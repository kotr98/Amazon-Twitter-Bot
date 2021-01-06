from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tweepy
from datetime import datetime
import time
import logging

#---------------------------Logger---------------------------

logging.basicConfig(filename='Logger.log',filemode='a',level=logging.INFO)

# ---------------------Twitter API Setup---------------------
auth = tweepy.OAuthHandler("enter api key here")
auth.set_access_token("enter token here")

api = tweepy.API(auth)


#--------------------Webcrawler Check---------------------
chrome_options = Options()
chrome_options.add_argument("--headless")

while True:
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)
    #driver.get("https://www.amazon.de/-/en/9399506/dp/B08H99BPJN/ref=sr_1_1?dchild=1&keywords=ps5&qid=1608477764&sr=8-1")#Controller
    driver.get("https://www.amazon.de/-/en/dp/B08H98GVK8/ref=sr_1_1?dchild=1&keywords=ps5&qid=1608405232&sr=8-1&th=1")
    #print("driver load ging")
    try:
        add_to_basket = driver.find_element_by_id('add-to-cart-button')
        kauf_exists = True
    except:
        kauf_exists = False
    driver.close()
    #print("driver.close ging")

    #----------------------Tweet absetzen----------------------
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if kauf_exists:
        api.update_status("{}: PS5 ist da".format(dt_string))
    else:
        logging.info("{}: Leider nicht da".format(dt_string))

    time.sleep(1800)
