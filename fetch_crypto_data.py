import requests
import pandas as pd 
import time
from dotenv import load_dotenv
import os


# Alpha Vantage API key

load_dotenv()
api_key = os.getenv('api_key')


# Function to fetch Bitcoin data
def fetch_crypto_data(symbol, market):
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if "Time Series (Digital Currency Daily)" in data:
        time_series = data['Time Series (Digital Currency Daily)']
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()

        return df
    else:
        print(f"Error fetching data for {symbol}: {data}")
        return pd.DataFrame()

# Fetch data for Bitcoin (BTC) in USD
bitcoin_data = fetch_crypto_data('BTC', 'USD')


#bitcoin_data.to_csv(r'/Users/ms/Desktop/CAB/DataPipeline/New Project/bitcoin_data.csv', index = None, header=True)
 

# Print data
print("Bitcoin Data (USD):")
print(bitcoin_data.head())