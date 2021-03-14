from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://twitter.com/login")

try:
    #Waits for the element to exist before continuing.
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session[username_or_email]"))
    )

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session[password]"))
    )

    #Change for your username and password here.
    username_field.send_keys(os.getenv("TWITTER_USERNAME"))
    password_field.send_keys(os.getenv("TWITTER_PASSWORD"))

    #Press enter once the fields are filled (You could also try to access the button element)
    password_field.send_keys(Keys.RETURN)

    tweet_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']/div/div/div/span"))
    )

    #Change the content of your tweet here.
    tweet_field.send_keys("This was tweeted by a Selenium bot.")

    tweet_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']"))
    )

    tweet_button.click()

except:
    driver.quit()
