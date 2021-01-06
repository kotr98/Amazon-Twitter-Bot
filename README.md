# Amazon-Twitter-Bot
This is a small bot which tweets if a product is available on amazon.

You can run this for example on a headless Raspberry Pi with necessary packages and drivers installed.<br/>
Also, you need the twitter API set up.<br/>
It will check every 30 minutes if the product is available and tweet it once it is available. <br/>

Following steps are necessary for setup on raspberry Pi: <br/>
1. sudo apt-get update
2. sudo apt-get install python3.7
3. sudo apt install python3-pip
4. pip3 install tweepy
5. pip3 install selenium
6. sudo apt-get install chromium-chromedriver
