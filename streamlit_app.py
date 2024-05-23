import streamlit as st
from psycopg2 import sql
from sqlalchemy import create_engine
import pandas as pd

# Function to get the connection to the database
def get_db_connection():
    DATABASE_URL = "postgresql://postgres:UBdSYyxDMmedlkApIyurYLqTPAnVPRCj@monorail.proxy.rlwy.net:30163/railway"
    engine = create_engine(DATABASE_URL)
    
    return engine


# Function to fetch bitcoin data from the database
def fetch_bitcoin_data(engine):
    query = "SELECT * FROM bitcoin_data ORDER BY date"
    df = pd.read_sql(query, engine)

    return df
    

# Function to fetch bitcoin news data from the database
def fetch_bitcoin_news(engine):
    query = "SELECT * FROM bitcoin_news"
    df = pd.read_sql(query, engine)
    return df


# Get the database connection
conn = get_db_connection()

# Fetch the bitcoin data and news
bitcoin_data_df = fetch_bitcoin_data(conn)
bitcoin_news_df = fetch_bitcoin_news(conn)


# Display Bitcoin data
st.title("Bitcoin Data")
st.line_chart(bitcoin_data_df.set_index('date')['close'])

# Display Bitcoin news
st.title("Bitcoin News")
st.write(bitcoin_news_df)
