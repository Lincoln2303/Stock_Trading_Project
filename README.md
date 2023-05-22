# Stock_Trading_Project

## Description

This is a Python script that fetches stock market data for a specific company, compares the closing prices of the stock on two different days, and sends a notification message if the percentage change exceeds a certain threshold.

## Technologies Used

- Python
- Alpha Vantage API for stock data retrieval
- News API for news articles retrieval
- Twilio for sending notification messages

## Installation

1. Get the necessary API keys:
  - Alpha Vantage API key for stock data retrieval
  - News API key for news articles retrieval
2. Clone the repository: git clone https://github.com/YourUsername/Stock_Trading_Notification.git
3. Replace the placeholder values in the script:
  - my_api_key: Replace with your Alpha Vantage API key.
  - API_KEY_NEWS: Replace with your News API key.
  - STOCK: Replace with the stock symbol you want to track.
  - COMPANY_NAME: Replace with the name of the company.
4. Install the required Python packages: pip install requests twilio
5. Run the script: python main.py

## Features

- User registration and authentication
- Stock market data retrieval using APIs
- Real-time stock prices and charts
- Portfolio management
- Buy and sell stocks
- Transaction history tracking

## Usage

- The script retrieves stock market data using the Alpha Vantage API and news articles using the News API.
- It compares the closing prices of the stock on two different days and calculates the percentage change.
- If the percentage change exceeds a certain threshold (e.g., 5%), it sends a notification message using the Twilio API.
- The notification message includes the stock price change percentage and the reason from the related news article.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
The project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course on Udemy by Dr. Angela Yu.
