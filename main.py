# we will be building a web scraper with selenium
# here we will be using the selenium webdriver to do web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.com/Smartwatch-Activity-Waterproof-Pedometer-Calories/dp/B0CYBVPW33/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.33f8f65b-b95c-44af-8b89-e59e69e79828&dib=eyJ2IjoiMSJ9.78Omlq8-6E4Xstcfnv5ItJtuNh6FpTIrputfb8zONgi0F-oeZePFM0-7ulKs-jrcycrF6riApX0_Os9uUCcUXa6WnWGACiTiRMLFxDLMuajojDpl0rxYtxrZMOAaUdhwlAMqsKc6PTOulL7PojglE4rH4xrFZcNIA3ehdz8_QFWsPLnlVMiiFALbfpdB2AKAp7VcEVoC6wOAYprlL1p_rKqqDtyS0qmrhSuCLHpREfw.uovRFLzGfJDIrFbEJW0Uqvm-veR3KolVCDNPrURwKJU&dib_tag=se&keywords=activity+trackers+and+smartwatches&pd_rd_r=f851c4d4-70d4-46be-884c-ed8b571ba25f&pd_rd_w=nvrEb&pd_rd_wg=AcF1e&pf_rd_p=33f8f65b-b95c-44af-8b89-e59e69e79828&pf_rd_r=5JWR9SZGZK7Q5XTD8P5T&qid=1723937516&sr=8-1')
# time.sleep(15)
# # noe we will select the element we need by the class name
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text
# print(f'the price is ${price_dollar}.{price_cents}')


# how to search by XPATH
# we will do this in the python.org website
# driver.get('https://www.python.org')
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute('href'))


# now we will trat the case where we need to find a lot of elements
# driver.find_elements(By.CLASS_NAME, 'btn-group')





driver.quit()
