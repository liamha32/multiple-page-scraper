from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# website = "https://quotes.toscrape.com/"
# path = "D:\chromedriver-win64\chromedriver.exe"
# driver = webdriver.Chrome()
# driver.get(website)
#
# quoting = driver.find_elements(By.XPATH, '//span[@class="text"]')
# author =  driver.find_elements(By.XPATH, '//small[@class="author"]')
#
# thequotes = []
# theauthor= []


place = 1
thequotes = []
theauthor = []
while place < 11:
    website = (f"https://quotes.toscrape.com/page/{str(place)}/")
    path = "D:\chromedriver-win64\chromedriver.exe"
    driver = webdriver.Chrome()
    driver.get(website)

    quoting = driver.find_elements(By.XPATH, '//span[@class="text"]')
    author = driver.find_elements(By.XPATH, '//small[@class="author"]')

    # thequotes = []
    # theauthor = []
    for i in quoting:
       i = i.text
       thequotes.append(i)
    for i in author:
        i = i.text
        theauthor.append(i)
    place = place + 1




lol = pd.DataFrame({'Quote':thequotes,'Author':theauthor})
lol.to_csv('allpages.csv',index=False)
print(lol)