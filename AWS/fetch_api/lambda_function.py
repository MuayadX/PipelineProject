import requests
import json
import os

def fetch_crypto_data(event, context):
    # Load the API key from environment variables
    api_key = os.getenv('API_KEY')
    symbol = 'BTC'
    market = 'USD'
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={api_key}'
    
    response = requests.get(url)
    data = response.json()

    if "Time Series (Digital Currency Daily)" in data:
        time_series = data['Time Series (Digital Currency Daily)']
        return {
            'statusCode': 200,
            'body': json.dumps(time_series)
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error fetching data for {symbol}: {data}")
        }