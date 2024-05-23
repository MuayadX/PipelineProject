import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# Function to scrape news titles and dates about Bitcoin from Financial Times
def scrape_bitcoin_news():
    # Initialize empty list to store news titles and dates
    news_data = []

    # Iterate over the last 100 days
    for i in range(100):
        # Calculate date
        date = datetime.now() - timedelta(days=i)
        formatted_date = date.strftime("%Y-%m-%d")

        # Financial Times URL for Bitcoin news on a specific date
        url = f"https://www.ft.com/search?q=Bitcoin&dateTo={formatted_date}&dateFrom={formatted_date}&page=1"
        
        # Send GET request to the URL
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all news titles on the page
        titles = soup.find_all('a', class_='js-teaser-heading-link')
        
        # Extract titles and append to news_data list along with the date
        for title in titles:
            news_data.append((formatted_date, title.text.strip()))
            
    # Convert list of tuples to DataFrame for further analysis
    news_df = pd.DataFrame(news_data, columns=['Date', 'Title'])

    return news_df

# Scrape Bitcoin news titles and dates
bitcoin_news_df = scrape_bitcoin_news()
print(bitcoin_news_df)

# Display DataFrame
#print("Bitcoin News Titles with Dates:")
#print(bitcoin_news_df.head())