import requests
import time
import json
import os

def sentimentScore_api(event, context):
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
                    # Extract the scores for each label directly
                    scores = {item['label']: item['score'] for item in response_data[0]}
                    results.append(scores)
                break
            except requests.exceptions.RequestException:
                time.sleep(3)
        time.sleep(3)

    # Add the sentiment results back to the original data
    for i, scores in enumerate(results):
        for label, score in scores.items():
            data[i][label] = round(score,2)  

    # Return the modified data as a JSON object
    return {
        "statusCode": 200,
        "body": data
    }
