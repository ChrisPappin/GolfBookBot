import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'putYourUsernameHere'
passwordStr = 'putYourPasswordHere'

browser = webdriver.Chrome()



browser.get(('LINK HERE'))

time.sleep(1)

nextButton = browser.find_element_by_id('2020-07-22')
nextButton.click()

time.sleep(1)



timeButton = browser.find_element_by_xpath("//div[@id='TWENF2020-07-22-07.30.00.00018']/a[1]")

timeButton.click()


