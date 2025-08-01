# ==============================================================================
# File: /project/__init__.py
# Location: /project/
# Purpose: Application factory. Initializes the Flask app and registers blueprints.
# ==============================================================================
from flask import Flask

def create_app():
    """
    Creates and configures an instance of the Flask application.
    This is the application factory pattern.
    """
    app = Flask(__name__, template_folder='../templates')

    # The config can be loaded from a file or environment variables for more complex apps
    # app.config.from_object('config.DevelopmentConfig')

    # Register the blueprints
    # A blueprint for stock-related routes
    from .routes.stock_routes import stock_bp
    app.register_blueprint(stock_bp, url_prefix='/api/stocks')

    @app.route("/")
    def index():
        return "Welcome to the Stock Data API! Try accessing /api/stocks/data"

    return app