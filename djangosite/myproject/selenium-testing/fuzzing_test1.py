from cmath import exp
from email import message
from unicodedata import name
from bitarray import test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import string
import random
import random_fuzzer 
import valid_fuzzer 




def valid_fuzz_front_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    # driver.implicitly_wait(5)
    time.sleep(2)
    search_hotel_btn= driver.find_element(By.NAME, "submitButton")
    search_hotel_box= driver.find_element(By.NAME, "destinationorhotel")
    checkin_box= driver.find_element(By.NAME, "checkin")
    checkout_box= driver.find_element(By.NAME, "checkout")
    room_box= driver.find_element(By.NAME, "roomsnumber")
    adult_box= driver.find_element(By.NAME, "adultsnumber")
    children_box= driver.find_element(By.NAME, "childrennumber")

    # search_hotel_box.send_keys("Singapore, Singapore")
    # time.sleep(2)
    search_hotel_box.send_keys(valid_fuzzer.generate_valid_country())
    time.sleep(3)
    search_hotel_box.send_keys(Keys.DOWN)
    time.sleep(1)
    search_hotel_box.send_keys(Keys.ENTER)

    time.sleep(2)
    checkin_box.send_keys(valid_fuzzer.generate_valid_date())
    time.sleep(2)
    checkout_box.send_keys(valid_fuzzer.generate_valid_date())
    time.sleep(2)
    room_box.send_keys(3)
    time.sleep(2)
    adult_box.send_keys(2)
    time.sleep(2)
    children_box.send_keys(4)
    time.sleep(2)
    search_hotel_btn.click()
    time.sleep(5)
    driver.quit()


# main test
valid_fuzz_front_page()