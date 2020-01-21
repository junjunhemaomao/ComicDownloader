from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.action_chains import
import time
import random

br = webdriver.Chrome()
url = br.get("http://www.mangabz.com/m10344/")
wait_time = random(0.1,1)
time.sleep(wait_time)
image = url.find_element_by_xpath("//*[(@id = "cp_image")]")
