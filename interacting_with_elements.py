from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# # first of just to know we can find elements by link text in python selenium.
# # for example let's got to google
# driver.get('https://www.wikipedia.com')
# # translate_to_shqip = driver.find_element(By.LINK_TEXT, value = 'Shqip')
# # translate_to_shqip.click()
# #done
#
# # now let's say we want to search in wikipedia
# search_box = driver.find_element(By.NAME, 'search')
# search_box.send_keys('Python')
# search_box.send_keys(Keys.ENTER) # this is used for the keys that are not letters and that have special functions



# now let's go for a challenge
# we have a page that the course teachers have created and we need to insert the first name, last name and email address
# than we need to press the sign up button

driver.get('https://secure-retreat-92358.herokuapp.com/')
first_name_box = driver.find_element(By.XPATH, '/html/body/form/input[1]')

last_name_box = driver.find_element(By.XPATH, '/html/body/form/input[2]')

email_box = driver.find_element(By.XPATH, '/html/body/form/input[3]')
first_name_box.send_keys('Albi')
time.sleep(2)
last_name_box.send_keys('Idrizi')
time.sleep(2)
email_box.send_keys('albiidrizi27@gmail.com')
time.sleep(2)

submit_button = driver.find_element(By.XPATH, '/html/body/form/button')
submit_button.click()

time.sleep(10)
driver.quit()