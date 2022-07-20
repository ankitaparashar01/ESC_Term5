from cmath import exp
from email import message
from os import link
from unicodedata import name
from bitarray import test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions  
from selenium.webdriver.support.expected_conditions import staleness_of
import time

def click_links_front_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)

    link_list= driver.find_elements(By.TAG_NAME, "a")
    #Get all links
    for l in link_list:
        print(l.text, ": ", l.get_attribute("href"))
    
    time.sleep(2)

    #click all links
    for l in link_list:
        l_attribute= l.get_attribute("href")
        print("Navigating to ", l_attribute)
        if(l_attribute == None):
            continue
        staleElementLoaded= True
        while(staleElementLoaded):
            try:
                driver.get(l_attribute)
                time.sleep(3)
                driver.back()
                time.sleep(2)
                link_list= driver.find_elements(By.TAG_NAME, "a")
                # print("navigated to ", )
                staleElementLoaded= False
            except exceptions.StaleElementReferenceException:
                staleElementLoaded= True



click_links_front_page()