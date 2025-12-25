import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.google.com"
response = requests.get(url)

if response.status_code == 200:
    html_response = response.text
    print("HTML response fetched successfully.")
else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")


soup = BeautifulSoup(html_response, 'html.parser')

print("Title of the webpage:", soup.title.string)