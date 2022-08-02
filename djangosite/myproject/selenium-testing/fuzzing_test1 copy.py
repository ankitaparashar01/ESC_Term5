from cmath import exp
from distutils.log import error
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

# initialize driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

error_list= [] # stores list of inputs that generate an error
pass_list= [] # stores list of inputs that pass

def invalid_fuzz_front_page():
    try:
        driver.get("http://127.0.0.1:8000/")
        print('driver Title:',driver.title)
        print('Driver name:',driver.name)
        print('Driver URL:',driver.current_url)
        # driver.implicitly_wait(5)

        # get elements of index page
        time.sleep(2)
        search_hotel_btn= driver.find_element(By.NAME, "submitButton")
        search_hotel_box= driver.find_element(By.NAME, "destinationorhotel")
        checkin_box= driver.find_element(By.NAME, "checkin")
        checkout_box= driver.find_element(By.NAME, "checkout")
        room_box= driver.find_element(By.NAME, "roomsnumber")
        adult_box= driver.find_element(By.NAME, "adultsnumber")
        children_box= driver.find_element(By.NAME, "childrennumber")

        # generate random data
        country= valid_fuzzer.generate_valid_country()
        checkin_date= valid_fuzzer.generate_valid_date()
        checkout_date= valid_fuzzer.generate_valid_date()
        rooms= valid_fuzzer.generate_valid_rooms()
        adults= valid_fuzzer.generate_valid_adults()
        children= valid_fuzzer.generate_valid_children()
        
        # input in website
        search_hotel_box.send_keys(country)
        time.sleep(2)
        search_hotel_box.send_keys(Keys.DOWN)
        # time.sleep(1)
        search_hotel_box.send_keys(Keys.ENTER)

        # time.sleep(2)
        checkin_box.send_keys(checkin_date)
        # time.sleep(2)
        checkout_box.send_keys(checkout_date)
        # time.sleep(2)
        room_box.send_keys(rooms)
        # time.sleep(2)
        adult_box.send_keys(adults)
        # time.sleep(2)
        children_box.send_keys(children)
        # time.sleep(2)
        search_hotel_btn.click()
        time.sleep(1)

        #try to find a page element to make sure it's still on the page. If fail, that means it's not on the page.
        search_hotel_btn_check= driver.find_element(By.NAME, "submitButton")
        pass_list.append([country, checkin_date, checkout_date, rooms, adults, children])

    except:
        print("Error occurred.")
        error_list.append([country, checkin_date, checkout_date, rooms, adults, children])
        # driver.refresh()
        # driver.quit()



def write_errors():
    fin= open("error_log.txt", mode='w', encoding='utf-8', newline="\n")
    for err in error_list:
        fin.write(str(err))
        fin.write("\n")
    fin.close()

def write_pass():
    fin= open("passed_log.txt", mode='w', encoding='utf-8', newline="\n")
    for p in pass_list:
        fin.write(str(p))
        fin.write("\n")
    fin.close()


# main function
def iterate_test(iter):
    for x in range(iter):
        invalid_fuzz_front_page()
    
    driver.quit()
    write_errors()
    write_pass()


# main test
# invalid_fuzz_front_page() #generates invalid and random input
# write_errors()

iterate_test(5)