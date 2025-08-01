# ==============================================================================
# File: /project/services/stock_service.py
# Location: /project/services/
# Purpose: Contains the business logic for fetching data from external sources.
# ==============================================================================
import yfinance as yf
import pandas as pd
import requests
import time
from datetime import datetime, timedelta
from config import ALPHA_VANTAGE_API_KEY, FMP_API_KEY # Import both API keys

def calculate_date_range(period):
    """Convert period string to from_date and to_date."""
    to_date = datetime.today()
    period_map = {
        "1d": timedelta(days=1), "5d": timedelta(days=5), "1mo": timedelta(days=30),
        "3mo": timedelta(days=90), "6mo": timedelta(days=180), "1y": timedelta(days=365),
        "2y": timedelta(days=730), "5y": timedelta(days=1825), "10y": timedelta(days=3650),
        "max": timedelta(days=36500)
    }
    delta = period_map.get(period, timedelta(days=30))
    from_date = to_date - delta
    return from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d')

def fetch_from_yfinance(ticker, period, interval):
    """Attempts to fetch data from yfinance."""
    try:
        data = yf.Ticker(ticker).history(period=period, interval=interval, auto_adjust=True)
        if not data.empty:
            data.reset_index(inplace=True)
            date_col = next((col for col in data.columns if 'Date' in str(col)), 'Date')
            data[date_col] = data[date_col].dt.strftime('%Y-%m-%d %H:%M:%S')
            return data[[date_col, 'Open', 'High', 'Low', 'Close', 'Volume']]
    except Exception as e:
        print(f"yfinance error for {ticker}: {e}")
    return None

def fetch_from_fmp(ticker, from_date, to_date):
    """Second fallback to fetch data from Financial Modeling Prep."""
    print(f"yfinance failed. Trying FMP for {ticker}...")

    if FMP_API_KEY == "YOUR_FMP_API_KEY_HERE":
        print("FMP API key is not set. Please add it to config.py.")
        return None

    # FMP API requires from and to dates and uses the .NS suffix for Indian stocks.
    params = {"from": from_date, "to": to_date, "apikey": FMP_API_KEY}
    try:
        response = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}", params=params)
        response.raise_for_status()
        json_data = response.json()

        historical_data = json_data.get("historical")
        if not historical_data:
            print(f"No FMP data for {ticker}. Response: {json_data}")
            return None

        df = pd.DataFrame(historical_data)
        df.rename(columns={"date": "Date", "open": "Open", "high": "High", "low": "Low", "close": "Close", "volume": "Volume"}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
        return df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    except Exception as e:
        print(f"FMP error for {ticker}: {e}")
    return None

def fetch_from_alpha_vantage(ticker, from_date, to_date):
    """Third fallback to fetch data from Alpha Vantage."""
    # Corrected: Reverting back to original Alpha Vantage ticker and parameters.
    av_ticker = ticker.replace('.NS', '.BSE') # Use the original logic
    print(f"FMP failed. Trying Alpha Vantage for {av_ticker}...")

    if ALPHA_VANTAGE_API_KEY == "YOUR_API_KEY_HERE":
        print("Alpha Vantage API key is not set.")
        return None

    params = {
        "function": "TIME_SERIES_DAILY", "symbol": av_ticker,
        "apikey": ALPHA_VANTAGE_API_KEY, "outputsize": "full"
    }
    try:
        response = requests.get("https://www.alphavantage.co/query", params=params)
        response.raise_for_status()
        json_data = response.json()
        time_series = json_data.get("Time Series (Daily)")
        if not time_series:
            print(f"No Alpha Vantage data for {av_ticker}. Response: {json_data.get('Note') or json_data}")
            return None
        records = []
        for date, v in time_series.items():
            if from_date <= date <= to_date:
                records.append({
                    "Date": date + " 00:00:00", "Open": float(v["1. open"]),
                    "High": float(v["2. high"]), "Low": float(v["3. low"]),
                    "Close": float(v["4. close"]), "Volume": int(v["5. volume"])
                })
        return pd.DataFrame(records)
    except Exception as e:
        print(f"Alpha Vantage error for {av_ticker}: {e}")
    return None

def get_stock_data(tickers, period="1mo", interval="1d"):
    """
    Fetches stock data with multiple fallbacks: yfinance -> FMP -> Alpha Vantage.
    Returns a dictionary of dictionaries, each containing data and source info.
    """
    from_date, to_date = calculate_date_range(period)
    results = {}
    for ticker in tickers:
        print(f"\nFetching data for {ticker}...")
        df = None
        source = "Not Found"

        df = fetch_from_yfinance(ticker, period, interval)
        if df is not None:
            source = "yfinance"
            print(f"✔️ Success: Got data from {source} for {ticker}")
        else:
            df = fetch_from_fmp(ticker, from_date, to_date)
            if df is not None:
                source = "Financial Modeling Prep (FMP)"
                print(f"✔️ Success: Got data from {source} for {ticker}")
            else:
                df = fetch_from_alpha_vantage(ticker, from_date, to_date)
                if df is not None:
                    source = "Alpha Vantage"
                    print(f"✔️ Success: Got data from {source} for {ticker}")
                else:
                    print(f"❌ Failed to fetch data for {ticker} from all sources.")

        if df is not None:
            results[ticker] = {
                'data': df.to_dict(orient='records'),
                'source': source
            }
        else:
            results[ticker] = {
                'data': [],
                'source': source
            }

        time.sleep(1.2)

    return results