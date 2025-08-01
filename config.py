# ==============================================================================
# File: config.py
# Location: /project/
# Purpose: Stores configuration variables for the application.
# ==============================================================================
# List of Indian stock tickers to fetch data for.
# '.NS' suffix is for the National Stock Exchange (NSE).
# '.BO' suffix is for the Bombay Stock Exchange (BSE).
INDIAN_STOCK_TICKERS = [
    #"RELIANCE.NS",
    #"TCS.NS",
    #"HDFCBANK.NS",
    #"INFY.NS",
    #"ICICIBANK.NS",
    #"HINDUNILVR.NS",
    #"SBIN.NS",
    #"BAJFINANCE.NS"
    "META"
]

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env


# IMPORTANT: Replace this with your actual Alpha Vantage API key.
# 1. Alpha Vantage API Key
# Get a free key from: https://www.alphavantage.co/support/#api-key
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


# 2. Financial Modeling Prep (FMP) API Key
# Get a free key from: https://site.financialmodelingprep.com/developer
FMP_API_KEY = os.getenv("FMP_API_KEY")
