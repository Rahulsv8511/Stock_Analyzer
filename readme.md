# Stock_Analyzer
This app just pulls US stock data and displays on a browser. This is some very basic work done only using vibe coding. I didn't write a single line of code. Just prompts from ChatGPT and Gemini till the application works. I will make more changes to it and keep pushing the code. Stay tuned. 
Indian Stock Data Fetcher
This project is a Flask-based web application that fetches and displays historical stock data for a list of predefined Indian tickers. It is designed with a multi-source fallback mechanism to ensure data retrieval even if one API fails. The application provides a simple web interface that renders the fetched data in a tabular, easy-to-read format.

Table of Contents
Project Overview

Features

File Structure

API Data Sources

Setup and Installation

Running the Application

Project Configuration

Project Overview
The core of this project is a Flask application that acts as a data aggregator. It fetches historical stock data for a list of Indian stock tickers (e.g., BAJFINANCE.NS, RELIANCE.NS) from multiple external APIs. The primary goal is to provide a robust solution by trying a series of data sources in a specific order: yfinance -> Financial Modeling Prep -> Alpha Vantage.

The fetched data is then rendered in an HTML table, providing a clean and organized view of the historical stock performance.

Features
Multi-Source Fallback: If the primary data source (yfinance) fails to retrieve data for a specific ticker, the application automatically tries the next available source.

Tabular Web Interface: Data is displayed in a user-friendly HTML table, making it easy to analyze stock trends.

Configurable Parameters: The period and interval for historical data can be passed as URL query parameters (e.g., /data?period=1y&interval=1wk).

Clear Data Source Identification: The application explicitly labels the data source used for each stock ticker in the output.

File Structure
The project follows a standard Flask application structure.

/project/
├── config.py
├── __init__.py
├── requirements.txt
├── templates/
│   └── stock_data.html
├── routes/
│   └── stock_routes.py
└── services/
    └── stock_service.py
config.py: Contains all the necessary configuration settings, including the list of stock tickers and API keys for the different data sources.

__init__.py: Initializes the Flask application and registers the blueprints.

requirements.txt: Lists all the Python dependencies required to run the project.

/templates/stock_data.html: An HTML template that uses Jinja2 to render the stock data in a tabular format.

/routes/stock_routes.py: Defines the API endpoints (/data) and handles the web requests. It calls the service layer to fetch data and then renders the HTML template.

/services/stock_service.py: Contains the core business logic. This is where the functions to fetch data from yfinance, Financial Modeling Prep, and Alpha Vantage are located. It implements the fallback logic and returns the structured data.

API Data Sources
The application uses the following APIs, prioritized in this order:

yfinance: A popular Python library that fetches historical market data from Yahoo Finance. This is the primary and most reliable source for this project.

Financial Modeling Prep (FMP): A financial API service. Note: As discovered during development, the free tier of FMP's "Historical Price Full" endpoint does not support non-US stock tickers. Requests for Indian stocks will result in a 403 Forbidden error. This fallback is therefore limited.

Alpha Vantage: A financial data API that provides a free plan. The free plan is often rate-limited and may have limitations on certain tickers or data points.

Setup and Installation
Prerequisites
Python 3.6 or higher

A virtual environment (recommended)

API keys for Financial Modeling Prep and Alpha Vantage (free plans are available)

Steps
Clone the repository (if applicable) or set up the project files.

Create a virtual environment and activate it:

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:

Bash

pip install -r requirements.txt
Configure API Keys:

Open the config.py file.

Replace the placeholder values with your actual API keys.

Note: As mentioned above, the FMP free plan does not support Indian stocks. You may need to leave its key placeholder empty or remove the fetch_from_fmp function if you only plan to use yfinance and Alpha Vantage.

Python

# File: /project/config.py
# ...
# 2. Financial Modeling Prep (FMP) API Key
# Note: Free plan may not support non-US stocks.
FMP_API_KEY = "YOUR_FMP_API_KEY_HERE"

# 3. Alpha Vantage API Key
ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY_HERE"
Running the Application
From the project's root directory, ensure your virtual environment is active.

Run the Flask application:

Bash

flask run
The application will start, and you will see output like:

 * Running on http://127.0.0.1:5000
Open your web browser and navigate to the following URL to see the tabular stock data:

http://127.0.0.1:5000/api/stocks/data
You can customize the period and interval by adding query parameters to the URL:

http://127.0.0.1:5000/api/stocks/data?period=5y

http://127.0.0.1:5000/api/stocks/data?period=1mo&interval=1h
