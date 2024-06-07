import datetime 
import psycopg2
import os 


def save_weather_todb(event, context):
    # Parse the Data as JSON
    #response = event   #this is just to Test the lambda function from the Test Event Json
    response = event['responsePayload'] #this to get the returned data from the 1st lambda function 
    
    # Database connection parameters
    DATABASE_URL = os.getenv('weather_db_url')
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)  
    # Connect to the PostgreSQL database
    cursor = conn.cursor()

    # Extract required fields
    dt = datetime.datetime.utcfromtimestamp(response.get('dt'))
    city = response.get('name')
    temp = round(response['main'].get('temp') - 273.15, 2)
    feels_like = round(response['main'].get('feels_like') - 273.15, 2)
    description = response['weather'][0].get('description')
        
    cursor.execute('''
        INSERT INTO weather_data (date, city, temp, feels, disc)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (date) DO NOTHING
    ''', (dt, city, temp, feels_like, description))

    conn.commit()
    cursor.close()
    conn.close()
    
    return "Data saved to Database successfully"