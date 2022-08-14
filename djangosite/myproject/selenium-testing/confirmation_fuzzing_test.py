# note- file must be ran in selenium-testing directory

from cmath import exp
from distutils.log import error
from email import message
from unicodedata import name
# from bitarray import test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import string
import random
import random_fuzzer 
import valid_fuzzer 

# this file inputs randomly valid inputs

# initialize driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

def setup_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

error_list= [] # stores list of inputs that generate an error
pass_list= [] # stores list of inputs that pass

######################################################################################################################################
# Test 0 - testing with valid inputs
######################################################################################################################################

def test0_confirmation_page():
    try:
        # load a confirmation page
        driver.get("http://127.0.0.1:8000/confirmation/dest_id=A6Dz/hotelName=Hotel%20Flavio%20Rome/hotelId=SPpa/roomKey=er-62AA84B7D5438C9F876DA1425B3D13C8-2EBF69C32423F4280F3FFB35267C8C32/roomType=200462189/checkin=Thursday,25%20August,2022/checkout=Monday,%2029%20August,%202022/guests=1/price=1067.82")
        print('Driver Title:',driver.title)
        print('Driver Title:',driver.title)
        print('Driver name:',driver.name)
        print('Driver URL:',driver.current_url)

        time.sleep(1)
        title_box= driver.find_element(By.NAME, "titleInput")
        first_name_box= driver.find_element(By.NAME, "firstNameInput")
        last_name_box= driver.find_element(By.NAME, "lastNameInput")
        country_code_box= driver.find_element(By.NAME, "countryCodeInput")
        phone_no_box= driver.find_element(By.NAME, "phoneNumberInput")
        message_box= driver.find_element(By.NAME, "messageInput")
        card_no_box= driver.find_element(By.NAME, "cardNumberInput")
        name_card_box= driver.find_element(By.NAME, "nameCardInput")
        expiry_month_box= driver.find_element(By.NAME, "expiryMonthInput")
        expiry_year_box= driver.find_element(By.NAME, "expiryYearInput")
        cvv_box= driver.find_element(By.NAME, "CVVInput")
        submit_btn= driver.find_element(By.NAME, "submitButton")

        title= valid_fuzzer.generate_valid_title()
        first_name= valid_fuzzer.generate_valid_firstname()
        last_name= valid_fuzzer.generate_valid_lastname()
        country_code= valid_fuzzer.generate_valid_countrycode()
        phone_number= valid_fuzzer.generate_valid_phonenumber()
        message= valid_fuzzer.generate_longmessage()
        card_number= valid_fuzzer.generate_valid_cardnumber()
        name_card= valid_fuzzer.generate_valid_fullname()
        expiry_month= valid_fuzzer.generate_valid_month()
        expiry_year= valid_fuzzer.generate_valid_year()
        cvv= valid_fuzzer.generate_valid_CVV()

        title_box.send_keys(title)
        first_name_box.send_keys(first_name)
        last_name_box.send_keys(last_name)
        country_code_box.send_keys(country_code)
        phone_no_box.send_keys(phone_number)
        message_box.send_keys(message)
        card_no_box.send_keys(card_number)
        name_card_box.send_keys(name_card)
        expiry_month_box.send_keys(expiry_month)
        expiry_year_box.send_keys(expiry_year)
        cvv_box.send_keys(cvv)
        submit_btn.click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(1)

        # find page element
        submit_btn_check= driver.find_element(By.NAME, "submitButton")
        print("Passed.\n")
        pass_list.append([title, first_name, last_name, country_code, phone_number, message, card_number, name_card, expiry_month, expiry_year, cvv])

    except:
        print("Error occurred.\n")
        error_list.append([title, first_name, last_name, country_code, phone_number, message, card_number, name_card, expiry_month, expiry_year, cvv])



######################################################################################################################################
# Test 1 - testing with random inputs
######################################################################################################################################

def test1_confirmation_page():
    try:
        # load a confirmation page
        driver.get("http://127.0.0.1:8000/confirmation/dest_id=A6Dz/hotelName=Hotel%20Flavio%20Rome/hotelId=SPpa/roomKey=er-62AA84B7D5438C9F876DA1425B3D13C8-2EBF69C32423F4280F3FFB35267C8C32/roomType=200462189/checkin=Thursday,25%20August,2022/checkout=Monday,%2029%20August,%202022/guests=1/price=1067.82")
        print('Driver Title:',driver.title)
        print('Driver name:',driver.name)
        print('Driver URL:',driver.current_url)

        time.sleep(1)
        title_box= driver.find_element(By.NAME, "titleInput")
        first_name_box= driver.find_element(By.NAME, "firstNameInput")
        last_name_box= driver.find_element(By.NAME, "lastNameInput")
        country_code_box= driver.find_element(By.NAME, "countryCodeInput")
        phone_no_box= driver.find_element(By.NAME, "phoneNumberInput")
        message_box= driver.find_element(By.NAME, "messageInput")
        card_no_box= driver.find_element(By.NAME, "cardNumberInput")
        name_card_box= driver.find_element(By.NAME, "nameCardInput")
        expiry_month_box= driver.find_element(By.NAME, "expiryMonthInput")
        expiry_year_box= driver.find_element(By.NAME, "expiryYearInput")
        cvv_box= driver.find_element(By.NAME, "CVVInput")
        submit_btn= driver.find_element(By.NAME, "submitButton")

        title= random_fuzzer.generate_random()
        first_name= random_fuzzer.generate_random()
        last_name= random_fuzzer.generate_random()
        country_code= random_fuzzer.generate_random()
        phone_number= random_fuzzer.generate_random()
        message= random_fuzzer.generate_random()
        card_number= random_fuzzer.generate_random()
        name_card= random_fuzzer.generate_random()
        expiry_month= random_fuzzer.generate_random()
        expiry_year= random_fuzzer.generate_random()
        cvv= random_fuzzer.generate_random()

        title_box.send_keys(title)
        first_name_box.send_keys(first_name)
        last_name_box.send_keys(last_name)
        country_code_box.send_keys(country_code)
        phone_no_box.send_keys(phone_number)
        message_box.send_keys(message)
        card_no_box.send_keys(card_number)
        name_card_box.send_keys(name_card)
        expiry_month_box.send_keys(expiry_month)
        expiry_year_box.send_keys(expiry_year)
        cvv_box.send_keys(cvv)
        submit_btn.click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(1)

        # find page element
        submit_btn_check= driver.find_element(By.NAME, "submitButton")
        print("Passed.\n")
        pass_list.append([title, first_name, last_name, country_code, phone_number, message, card_number, name_card, expiry_month, expiry_year, cvv])

    except:
        print("Error occurred.\n")
        error_list.append([title, first_name, last_name, country_code, phone_number, message, card_number, name_card, expiry_month, expiry_year, cvv])

######################################################################################################################################
# HELPER FUNCTIONS
######################################################################################################################################
def write_errors(filein):
    fin= open(filein, mode='w', encoding='utf-8', newline="\n")
    for err in error_list:
        fin.write(str(err))
        fin.write("\n")
    fin.close()
    error_list.clear() # empty error list
    

def write_pass(filein):
    fin= open(filein, mode='w', encoding='utf-8', newline="\n")
    for p in pass_list:
        fin.write(str(p))
        fin.write("\n")
    fin.close()
    pass_list.clear() # empty pass list


def iterate_test0(iter):
    for x in range(iter):
        test0_confirmation_page()
    # driver.close()
    write_errors("logs/confirmation_error_log_test0.txt")
    write_pass("logs/confirmation_passed_log_test0.txt")

def iterate_test1(iter):
    for x in range(iter):
        test1_confirmation_page()
    # driver.close()
    write_errors("logs/confirmation_error_log_test1.txt")
    write_pass("logs/confirmation_passed_log_test1.txt")

# def iterate_test2(iter):
#     for x in range(iter):
#         test2_front_page()
#     # driver.close()
#     write_errors("logs/error_log_test2.txt")
#     write_pass("logs/passed_log_test2.txt")

# main test
# invalid_fuzz_front_page() #generates invalid and random input
# write_errors()

######################################################################################################################################
# MAIN FUNCTION
######################################################################################################################################
def main_function(): 
    print("============ starting test 0 ============")
    iterate_test0(5)
    setup_driver()

    print("============ starting test 1 ============")
    iterate_test1(5)
    setup_driver()
    
    # print("============ starting test 2 ============")
    # iterate_test2(5)
    driver.quit()

main_function()