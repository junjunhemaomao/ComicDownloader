import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

response = requests.get('http://www.mangabz.com/m10344/').content.decode()
img = re.findall('(i?)<img.*? src=\"?(.*?\\.(jpg|gif|bmp|bnp|png))\".*? />',response)
print(img)