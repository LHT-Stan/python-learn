import requests
from bs4 import BeautifulSoup

url = "https://cd.lianjia.com/"
response = requests.get(url)

# Set the correct character encoding for the website
response.encoding = "utf-8"  # Replace "utf-8" with the correct character encoding

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Extract the data you need from the website
data = soup.find_all("p")  # Replace "p" with the HTML element you want to extract
data = data + soup.find_all("div")
# Print the data
for element in data:
    print(element.text)





