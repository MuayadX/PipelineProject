import requests
import os

API_URL = os.getenv('url')
token = os.getenv('token')
headers = {"Authorization": f"Bearer {token}"}

def lambda_handler(event, context):
    # Extract the news data from the event
    news_data = event.get('news_data', {}).get('body', []) # for testing use news_data instead of responsePayload (which is a required field by AWS Lambda)
    
    # Initialize a list to store the results
    results = []
    
    # Iterate through the news data and perform sentiment analysis
    for item in news_data:
        title = item['Title']
        response = requests.post(API_URL, headers=headers, json={"inputs": title})
        sentiment_result = response.json()
        
        # Flatten the sentiment result
        flattened_sentiment = {sentiment['label']: sentiment['score'] for sentiment in sentiment_result[0]}
        
        results.append({
            "Date": item["Date"],
            "Title": title,
            **flattened_sentiment
        })
    
    # Return the results
    return {
        "statusCode": 200,
        "body": results
    }