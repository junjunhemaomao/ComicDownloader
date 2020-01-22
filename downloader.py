from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep
import requests
import time
import random


web = webdriver.Chrome()
web.get("http://www.mangabz.com/m10344/")
wait = WebDriverWait(web,10)
#wait_time = random(0.1,1)
#time.sleep(wait_time)
img = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'img')))
actions = ActionChains(web)
actions.context_click(img)
actions.perform()
pyautogui.typewrite(['down','down','down','down','down','down','down','enter','enter'])
sleep(0.2)
pyautogui.typewrite(['enter'])