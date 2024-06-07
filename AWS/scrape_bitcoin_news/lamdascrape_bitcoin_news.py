import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

def scrape_bitcoin_news(event, context):
    news_data = []

    for i in range(100):
        date = datetime.now() - timedelta(days=i)
        formatted_date = date.strftime("%Y-%m-%d")

        url = f"https://www.ft.com/search?q=Bitcoin&dateTo={formatted_date}&dateFrom={formatted_date}&page=1"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('a', class_='js-teaser-heading-link')

        for title in titles:
            news_data.append({"date": formatted_date, "title": title.text.strip()})

    return {
        "statusCode": 200,
        "body": news_data
    }
    
    
    
    