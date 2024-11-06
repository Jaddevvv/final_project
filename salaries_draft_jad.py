import os
import pandas as pd
import matplotlib.pyplot as plt
import time
# import re
# import requests
# from bs4 import BeautifulSoup
# from currency_converter import CurrencyConverter
# import the required libraries








from selenium import webdriver
from selenium.webdriver.common.by import By
import re 

# instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# initialize an instance of the chrome driver (browser) in headless mode
driver = webdriver.Chrome(
    options=options,
)

# visit your target site
driver.get("https://www.oanda.com/currency-converter/live-exchange-rates/")

# extract all the product containers
rates = driver.find_elements(By.XPATH, "/html/body/div[1]/main/div/div/div[3]")

time.sleep(3)

def get_rate(rate):
  rate_pair = rate + "/EUR"
  for rate in rates:
    if rate_pair in rate.text:
      return float(rate.text.split(rate_pair)[1].split("\n")[1] + rate.text.split(rate_pair)[1].split("\n")[2])


pair_list = ['USD', 'GBP', 'CAD', 'AUD','NZD', 'CHF', 'ZAR', 'SEK', 'HKD', 'JPY']  
exchange_rate = {}
for pair in pair_list:
  exchange_rate[pair] = get_rate(pair)

print(exchange_rate)




# pd.options.display.max_columns = 200
# pd.options.display.max_rows = 3000

# def parent_directory():

#   # Create a relative path to the parent
#   # of the current working directory
#   relative_parent = os.path.join(os.getcwd(), os.pardir)
#   # Return the absolute path of the parent directory
#   return os.path.abspath(relative_parent)

# print(parent_directory())

# def str_2_int(value):
#   if ',' in value:
#     x = float(value.replace(',',''))
#     return x
#   else :
#     return float(value)




# # For Google Colab the ability to read csv from parent_directory is different so I modified it
# salaries = pd.read_csv('./0.Ressources/05_2_salaries.csv')

# #Rename Column names because they were too long
# salaries.columns = ['Time', 'Age', 'Industry', 'Job', 'Job Context', 'Salary', 'Bonus', 'Currency', 'Other Currency', 'Income Context', 'Country', 'US State', 'City', 'Experience', 'Field experience', 'Education', 'Gender', 'Race']

# #Convert String to float
# salaries["Salary"] = salaries["Salary"].apply(str_2_int)


# #Replace NA values in Bonus by 0 and add a "Total Remuneration" Column
# values = {"Bonus": 0.0}
# salaries = salaries.fillna(value = values)
# salaries["Total Remuneration"] = salaries["Salary"] + salaries["Bonus"]
# move = salaries.pop("Total Remuneration")
# salaries.insert(7,"Total Remuneration" ,move)


# salaries["Time"] = pd.to_datetime(salaries["Time"], format='%m/%d/%Y %H:%M:%S')

# # c = CurrencyConverter()
# # value = c.convert(100, 'USD', 'EUR')
# # print(value)

# response = requests.get("https://www.oanda.com/currency-converter/live-exchange-rates/")
# soup = BeautifulSoup(response.text, 'html.parser')

# rate = soup.find_all('span',class_="symbol yf-138ga19")
# print(response.text)