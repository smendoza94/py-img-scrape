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
print('Number of images found:', len(img_tags))

# create a directory to store the images
if not os.path.exists('images'):
    os.makedirs('images')

# download each image and save it in the images directory/folder
for img_tag in img_tags: 
    img_url = img_tag['src'] # extract the image URL
    img_data = os.path.basename(img_url).split('?')[0]  # extract filename and remove query params
    with open(os.path.join('images', img_data), 'wb') as handler: # open the file in write binary mode
        img = requests.get(img_url)   # make a GET request to the image URL
        handler.write(img.content)  # write the image content to the file

# print the total number of images downloaded
print('Total images downloaded:', len(img_tags))