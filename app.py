# ==============================================================================
# File: run.py
# Location: root of your project directory
# Purpose: The main entry point to start the Flask application.
# ==============================================================================
from project import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == '__main__':
    # When you run this file directly, it starts the development server.
    # host='0.0.0.0' makes the server accessible from other devices on your network.
    # debug=True enables the interactive debugger and reloads the server on code changes.
    # For production, you would use a proper WSGI server like Gunicorn.
    app.run(host='0.0.0.0', port=5000, debug=True)