import requests

html_str = requests.get('https://www.baidu.com').content.decode()

