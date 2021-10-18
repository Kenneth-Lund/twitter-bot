from selenium import webdriver
from models.models import TwitterUser
from models.models import Parameters
from models.models import Tweet
from datetime import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

LOGIN_ROUTE = 'https://twitter.com/i/flow/login'
TRENDING_ROUTE = 'https://twitter.com/explore/tabs/trending'

# Logs in and posts a tweet
def login(driver: webdriver, parameters: Parameters) -> TwitterUser:

    username = parameters.username
    password = parameters.password

    driver.get(LOGIN_ROUTE)
    time.sleep(1)
    
    # TODO: Try catches implemented here would handle any future error handling. Returns None for now for prototype implementation.
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(username)
        time.sleep(2)
    except:
        return None

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(Keys.RETURN)
        time.sleep(2)
    except:
        return None

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
        time.sleep(2)
    except:
        return None

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(Keys.RETURN)
        time.sleep(2)
    except:
        return None

    time.sleep(2)
    
    # Returns Twitter user object once log in is successful
    return TwitterUser(username, datetime.now())

# Uses webdriver object to submit a post.
# TODO: Error handling
def submit_post(driver: webdriver, user: TwitterUser) -> Tweet:
    
    tweet_text_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    driver.find_element_by_xpath(tweet_text_xpath).send_keys("I wanna move to Texas.")
    time.sleep(2)

    upload_image_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/input'
    driver.find_element_by_xpath(upload_image_xpath).send_keys("/Users/kennethlund/Desktop/mask.io/twitter_bot/media/helpmemovetotexas.jpg")
    time.sleep(2)

    tweet_submit_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]'
    driver.find_element_by_xpath(tweet_submit_xpath).click()
    time.sleep(20)
    
    # Returns a Tweet object once a tweet is successfully submitted.
    return Tweet("", user.username, "")
