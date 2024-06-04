
import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def save_crypto_data(event):
    # Simulated event data for testing
    event = '''{
        "statusCode": 200,
        "body": "{\\"2025-05-31\\": {\\"1. open\\": \\"68338.58000000\\", \\"2. high\\": \\"68438.78000000\\", \\"3. low\\": \\"68280.11000000\\", \\"4. close\\": \\"68351.27000000\\", \\"5. volume\\": \\"78.34317404\\"}, \\"2025-05-30\\": {\\"1. open\\": \\"67569.44000000\\", \\"2. high\\": \\"69536.89000000\\", \\"3. low\\": \\"67092.91000000\\", \\"4. close\\": \\"68338.58000000\\", \\"5. volume\\": \\"11841.26381893\\"}}"
    }'''
    
    # Parse the outer JSON
    jsonf = json.loads(event)
    
    # Extract the body field and parse it as JSON
    data = json.loads(jsonf["body"])
    
    # Database connection parameters
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # Database connection details
    db_host = os.getenv('host')
    db_port = os.getenv('port')
    db_name = os.getenv('database')
    db_user = os.getenv('user')
    db_password = os.getenv('password')
    
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )

    # Connect to the PostgreSQL database
    #conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Insert data into the database
    for date, values in data.items():
        open_value = values['1. open']
        high_value = values['2. high']
        low_value = values['3. low']
        close_value = values['4. close']
        volume_value = values['5. volume']
        
        cursor.execute('''
            INSERT INTO bitcoin_data (date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        ''', (date, open_value, high_value, low_value, close_value, volume_value))

    conn.commit()
    cursor.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }
    
    
event = '''{
        "statusCode": 200,
        "body": "{\\"2025-05-31\\": {\\"1. open\\": \\"68338.58000000\\", \\"2. high\\": \\"68438.78000000\\", \\"3. low\\": \\"68280.11000000\\", \\"4. close\\": \\"68351.27000000\\", \\"5. volume\\": \\"78.34317404\\"}, \\"2025-05-30\\": {\\"1. open\\": \\"67569.44000000\\", \\"2. high\\": \\"69536.89000000\\", \\"3. low\\": \\"67092.91000000\\", \\"4. close\\": \\"68338.58000000\\", \\"5. volume\\": \\"11841.26381893\\"}}"
    }'''
    
save_crypto_data(event)