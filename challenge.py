from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
pd.set_option('display.max_colwidth', None)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')
driver.maximize_window()

table_title = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/h2').text
print(table_title)

dates = driver.find_elements(By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/time')
dates_list = []
for date in dates:
    print(date.text)
    dates_list.append(date.text)


event_names = driver.find_elements(By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/a')
event_links = []
event_names_list = []
for event in event_names:
    event_links.append(event.get_attribute('href'))
    event_names_list.append(event.text)


print(dates_list)
print(event_links)
print(event_names_list)

# # to create a matrix with dataframes we need a dictionary first
# dict = {
#     'Dates': dates_list,
#     'Event Links': event_links,
#     'Event Names': event_names_list
# }
# matrix = pd.DataFrame(dict)
# print(len(dates_list))
# print(len(event_links))
# print(len(event_names_list))
# print(matrix)

# Inspect the first few links to ensure they are correct
for link in event_links[:5]:
    print(repr(link))


# Check if lists are of the same length
if len(dates_list) == len(event_names_list) == len(event_links):
    # Create a DataFrame
    data = {
        'Dates': dates_list,
        'Event Links': event_links,
        'Event Names': event_names_list
    }
    matrix = pd.DataFrame(data)
    print(matrix)
else:
    print("Error: Mismatch in the length of extracted lists.")
    print(f"Dates: {len(dates_list)}, Event Names: {len(event_names_list)}, Event Links: {len(event_links)}")













driver.quit()



