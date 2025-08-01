# 📊 Financial Data Viewer (Flask App)

This is a simple Flask web application that displays financial data using APIs like Alpha Vantage and Financial Modeling Prep (FMP).

## 🚀 Features

- Fetches real-time stock data
- Uses two external APIs: Alpha Vantage and FMP
- Securely loads API keys from environment variables
- Easy to run locally

## 🛠️ Setup Instructions

1. Clone the Repository  
   `git clone https://github.com/yourusername/flask-app.git`  
   `cd flask-app`

2. Create a Virtual Environment (Optional but Recommended)  
   `python -m venv venv`  
   `source venv/bin/activate`  *(On Windows: `venv\Scripts\activate`)*

3. Install Dependencies  
   `pip install -r requirements.txt`

## 🔐 Environment Variables

This app uses a `.env` file to store API keys securely.

1. Create a `.env` File  
   Add the following:

   ```
   ALPHA_VANTAGE_API_KEY=your-alpha-vantage-key
   FMP_API_KEY=your-fmp-api-key
   ```

2. Get Your API Keys  
   - Alpha Vantage: https://www.alphavantage.co/support/#api-key  
   - Financial Modeling Prep: https://financialmodelingprep.com/developer/docs

## 🧪 Run the App

`python app.py`

Then open your browser and go to:  
`http://127.0.0.1:5000/`

## 📁 Project Structure

```
flask-app/
├── app.py
├── config.py
├── templates/
├── static/
├── .env
├── .gitignore
└── README.md
```

## 🛡️ Security Notes

- Never commit your `.env` file to GitHub  
- Use `.env.example` to show required variables without exposing secrets

## 🙌 Contributing

Feel free to fork the repo, open issues, or submit pull requests!

## 📄 License

This project is licensed under the MIT License.