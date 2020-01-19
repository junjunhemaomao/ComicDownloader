import requests

#获取网页源代码
source = requests.get('http://www.mangabz.com/m10344/').content.decode()

