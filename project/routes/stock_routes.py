# ==============================================================================
# File: /project/routes/stock_routes.py
# Location: /project/routes/
# Purpose: Defines the API endpoints (routes) related to stocks.
# ==============================================================================
from flask import Blueprint, jsonify, request, render_template
from ..services import fetch_stock_data
import config # Import the config file

# A Blueprint is a way to organize a group of related views and other code.
# It's a key component for building modular Flask applications.
stock_bp = Blueprint('stock_routes', __name__)

@stock_bp.route('/data', methods=['GET'])
def get_all_stock_data():
    """
    API endpoint to get historical data for the predefined list of stocks.
    It can be customized with query parameters.
    Example URL: /api/stocks/data?period=5d&interval=1h
    """
    # Get tickers from the configuration file
    tickers = config.INDIAN_STOCK_TICKERS
    
    # Allow overriding period and interval via URL query parameters for flexibility
    period = request.args.get('period', default="1mo", type=str)
    interval = request.args.get('interval', default="1d", type=str)

    # Call the service layer to get the data
    data = fetch_stock_data.get_stock_data(tickers, period, interval)

    if not data:
        return jsonify({"error": "Could not retrieve stock data."}), 500
    return render_template('initial_stock_data.html', stock_data=data)

# You can keep the original route for a JSON output if you want to offer both
# @stock_bp.route('/json_data', methods=['GET'])
# def get_json_stock_data():
#     """
#     API endpoint to get historical data in JSON format.
#     """
#     tickers = config.INDIAN_STOCK_TICKERS
#     period = request.args.get('period', default="1mo", type=str)
#     interval = request.args.get('interval', default="1d", type=str)
#
#     data = stock_service.get_stock_data(tickers, period, interval)
#
#     if not data:
#         return jsonify({"error": "Could not retrieve any stock data. Check logs for details."}), 500
#
#     return jsonify(data)