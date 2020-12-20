
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tweepy
from datetime import datetime
import time

# ---------------------Twitter API Setup---------------------
auth = tweepy.OAuthHandler("enter api key here")
auth.set_access_token("enter token hier")

api = tweepy.API(auth)


#--------------------Webcrawler Check---------------------
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
driver.get("enter amazon link here (english)")

var = True
while var:
    try:
        add_to_basket = driver.find_element_by_id('add-to-cart-button')
        kauf_exists = True
    except:
        kauf_exists = False
    driver.close()


    #----------------------Tweet absetzen----------------------
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if kauf_exists:
        api.update_status("{}: It is available!".format(dt_string))
        var = False
    else:
        #print("{}: Not available".format(dt_string))

    time.sleep(600)