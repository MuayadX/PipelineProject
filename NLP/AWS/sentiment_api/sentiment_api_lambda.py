import requests
import time
import json
import os

def lambda_handler(event, context):
    model_id = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
    api_token =  os.getenv('HUGGING_FACE_API_TOKEN')

    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
    results = []

    # Parse the input JSON
    #data = event['body']
    data = event['responsePayload']['body']
    headlines = [item['title'] for item in data]

    # Initial wait before starting the queries
    time.sleep(5)

    for headline in headlines:
        while True:
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": headline})
                response_data = response.json()
                if response_data:
                    top_label = response_data[0][0]['label']
                    results.append(top_label)
                break
            except requests.exceptions.RequestException:
                time.sleep(3)
        time.sleep(3)

    # Add the sentiment results back to the original data
    for i, sentiment in enumerate(results):
        data[i]['sentiment'] = sentiment

    # Return the modified data as a JSON object
    return {
        "statusCode": 200,
        "body": data
    }
