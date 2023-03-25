# Py Image Scrapper/Download

### Description

1. This code specifies the URL of the website to scrape.
2. It makes a request to the website using the requests library and gets the HTML content of the website.
3. It parses the HTML content of the website using the BeautifulSoup library.
4. It finds all the image tags (<img>) on the website using the find_all() method of the BeautifulSoup object.
5. It creates a directory called "images" to store the image files.
6. It loops through each image tag, gets the URL of the image (src attribute), and downloads the image using the requests library.
7. It saves the image file in the "images" directory/folder with a name based on the URL of the image.

## Technology

This python code utilizes the following py modules

- [os](https://docs.python.org/3/library/os.html) to access operating system dependent functionality such as read and write files and directories/folders.
- [requests](https://pypi.org/project/requests/) to make HTTP requests.
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape information from web pages.

### _Dev Note_

_Note: that this script assumes that all the images on the website are directly linked in img tags with the src attribute._
