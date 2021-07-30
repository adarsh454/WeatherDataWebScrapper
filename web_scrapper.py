import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get(f'https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YP5f5ugzZPY')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id ='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
print(period_names)
weather_stuff = pd.DataFrame(
    {
        'Period':period_names,
        'short_description':short_descriptions,
        'Temperatures':temperatures
    })
print(weather_stuff)

weather_stuff.to_csv('weather.csv')
