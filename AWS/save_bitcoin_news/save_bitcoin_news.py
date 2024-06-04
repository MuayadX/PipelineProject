import json
import psycopg2
import os

def save_bitcoin_news(event, context):
    # Parse the body field as JSON
    news_data = json.loads(event['body'])
    #news_data = json.loads(event['responsePayload']['body'])

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
    
    for news in news_data:
        cursor.execute('''
            INSERT INTO bitcoin_news_aws(date, title)
            VALUES (%s, %s)
            ON CONFLICT (date) DO NOTHING
        ''', (news['date'], news['title']))
            
    conn.commit()
    cursor.close()
    conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }
    