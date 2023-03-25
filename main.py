import os
import requests
from bs4 import BeautifulSoup

# specify the URL of the website
url = input("> Enter a website's exact url page to extract the images from: ")

# try to make a GET request to the specified URL, passing the 's' query parameter 
# to search for 'requests+language:python'. if an exception occurs during the 
# request (e.g. connection error or timeout), catch the exception and print the 
# error message
try:
    response = requests.get(url, params={'s': 'requests+language:python'}) # make a GET request to the specified URL
    response.raise_for_status()  # raise an exception if the response status code is not 200 (OK)
except requests.exceptions.RequestException as error: # catch any RequestException
    raise SystemExit(error)  # exit the program with the error message

# parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')
# find all image tags on the website
img_tags = soup.find_all('img')
