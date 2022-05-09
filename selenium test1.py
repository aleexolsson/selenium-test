

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import re
import os
import gpio as GPIO

chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("disable-setuid-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(chrome_options=chrome_options)
print("hejhej")
driver.get("file:///home/alex/Documents/GitHub/info-table/project-fruit/index.html")

GPIO.cleanup