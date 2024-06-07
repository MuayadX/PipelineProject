import json
import psycopg2
import os

def save_sentimentScore(event, context):
    # Parse the body field as JSON
    #news_data = event['body']
    news_data = event['responsePayload']['body']
    
    # Database connection parameters
    DATABASE_URL = os.getenv('DATABASE_URL')
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    for news in news_data:
        cursor.execute('''
            INSERT INTO BitcoinNews_SentimentScore(date, title, neutral, negative, positive)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (title) DO NOTHING
        ''', (news['date'], news['title'], news['neutral'], news['negative'], news['positive']))
            
    conn.commit()
    cursor.close()
    conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }
    