# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


# options from internet to display all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


city = input('Enter the city you want to search for: ').strip().lower()
price = input('Enter the price you want to search for: ').strip().lower()


# we are going to create a web scraper that will scrape the house prices in Albania from the website Century21
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get('https://www.century21albania.com/')


city_search = driver.find_element(By.XPATH, value='//*[@id="search"]')
city_search.send_keys(city)
# first 'kerko' button
search_city_button = driver.find_element(By.XPATH, value='//*[@id="home"]/div/div[4]/button')
search_city_button.click()

# this code will make it to search for houses for sale
sale_filter_arrow = driver.find_element(By.XPATH, value='//*[@id="search-form"]/div/div[2]/div/span/span[1]/span/span[2]')
sale_filter_arrow.click()
sale_filter = driver.find_element(By.XPATH, value='/html/body/span/span/span[1]/input')
sale_filter.send_keys('shitje')
sale_filter.send_keys(Keys.ENTER)

city_filter_arroe = driver.find_element(By.XPATH, value='//*[@id="search-form"]/div/div[5]/div/span/span[1]/span/span[2]')
city_filter_arroe.click()
city_filter_searcher = driver.find_element(By.XPATH, value='/html/body/span/span/span[1]/input')
city_filter_searcher.send_keys(city)
city_filter_searcher.send_keys(Keys.ENTER)

# this will be used to enter the price
price_filter = driver.find_element(By.XPATH, value='//*[@id="search-form"]/div/div[11]/div/input')
price_filter.click()
price_filter.send_keys(price)
price_filter.send_keys(Keys.ENTER)


# this is to press the kerko button
search_button = driver.find_element(By.XPATH, value='//*[@id="search-form"]/div/div[12]/div/button')
search_button.click()

prices = []
titles = []
links = []
while True:

    # Generalizing XPath for all links within the divs (learned from the chat gpt)
    xpath = "/html/body/div/section[1]/div/div/div/section/div/div/div/div[2]/div[*]/div/a[2]"
    links_web = driver.find_elements(By.XPATH, xpath)
    for link in links_web:
        links.append(link.get_attribute('href'))

    card_bodies = driver.find_elements(By.CLASS_NAME, 'card-body')
    for card_body in card_bodies:
        prices.append(card_body.find_element(By.TAG_NAME, 'h2').text)
        titles.append(card_body.find_element(By.CLASS_NAME, 'card-title').text)

    # Check for the "Next" button and click it
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@rel="next"]')))
        next_button.click()
        time.sleep(5)  # Wait for new content to load e vene 5 sa persiguri
    except Exception as e:
        print("No more pages or error:", e)
        break

dict = {
    'Titles': titles,
    'Prices': prices,
    'Links': links
}

matrix = pd.DataFrame(dict)
print(matrix)

matrix.to_csv(f'{city}_property_listings.csv', index=False)


driver.quit()

