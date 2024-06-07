import json
import psycopg2
import os

def save_bitcoin_news_sentiment(event, context):
    # Parse the body field as JSON
    news_data = event['body']
    #news_data = event['responsePayload']['body']
    
    # Database connection parameters
    DATABASE_URL = os.getenv('DATABASE_URL')
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    for news in news_data:
        cursor.execute('''
            INSERT INTO bitcoin_news_sentiment(date, title, sentiment)
            VALUES (%s, %s, %s)
            ON CONFLICT (date) DO NOTHING
        ''', (news['date'], news['title'], news['sentiment']))
            
    conn.commit()
    cursor.close()
    conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }
    