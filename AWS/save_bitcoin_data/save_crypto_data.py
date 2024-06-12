import json
import psycopg2
import os

def save_crypto_data(event, context):
    # Parse the body field as JSON
    data = json.loads(event['responsePayload']['body'])
    
    # Database connection parameters from environment variables
    db_port = os.getenv('port')
    db_host = os.getenv('host')
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
    cursor = conn.cursor()

    # Insert data into the database
    for date, values in data.items():
        open_value = values['1. open']
        high_value = values['2. high']
        low_value = values['3. low']
        close_value = values['4. close']
        volume_value = values['5. volume']
        
        cursor.execute('''
            INSERT INTO bitcoin_data_aws (date, open, high, low, close, volume)
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
    




