from cmath import exp
from email import message
from unicodedata import name
from bitarray import test
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_front_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    # driver.implicitly_wait(5)
    time.sleep(2)
    search_hotel_btn= driver.find_element(By.NAME, "submitButton")
    search_hotel_box= driver.find_element(By.NAME, "destinationInput")
    checkin_box= driver.find_element(By.NAME, "checkinInput")
    checkout_box= driver.find_element(By.NAME, "checkoutInput")
    room_box= driver.find_element(By.NAME, "roomInput")
    adult_box= driver.find_element(By.NAME, "adultInput")
    children_box= driver.find_element(By.NAME, "childrenInput")

    search_hotel_box.send_keys("Singapore")
    time.sleep(2)
    checkin_box.send_keys("09072022")
    time.sleep(2)
    checkout_box.send_keys("11072022")
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

def test_hotellist_card():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/hotellistings/dest_id=A6Dz")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    # driver.implicitly_wait(5)
    time.sleep(2)
    # for now not implemented yet
    search_hotel_btn= driver.find_element(By.NAME, "submitButton")
    search_hotel_box= driver.find_element(By.NAME, "destinationInput")
    checkin_box= driver.find_element(By.NAME, "checkinInput")
    checkout_box= driver.find_element(By.NAME, "checkoutInput")
    room_box= driver.find_element(By.NAME, "roomInput")
    adult_box= driver.find_element(By.NAME, "adultInput")
    children_box= driver.find_element(By.NAME, "childrenInput")

    search_hotel_box.send_keys("Singapore")
    time.sleep(2)
    checkin_box.send_keys("09072022")
    time.sleep(2)
    checkout_box.send_keys("11072022")
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
    
def test_hotellist_select():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/hotellistings/dest_id=A6Dz")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    time.sleep(2)
    # driver.implicitly_wait(5)
    see_details_btn= driver.find_element(By.NAME, "seeDetailsButton")
    time.sleep(2)
    see_details_btn.click()

    time.sleep(3)
    driver.quit()
    
def test_confirmation_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/confirmation/")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    time.sleep(2)

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

    title_box.send_keys("Mr.")
    time.sleep(2)
    first_name_box.send_keys("Bob")
    time.sleep(2)
    last_name_box.send_keys("Aliceson")
    time.sleep(2)
    country_code_box.send_keys("+65")
    time.sleep(2)
    phone_no_box.send_keys("9182391")
    time.sleep(2)
    message_box.send_keys("Clean up the room thoroughly, I am allergic to dust.")
    time.sleep(2)
    card_no_box.send_keys(12934981893913)
    time.sleep(2)
    name_card_box.send_keys("Bob Aliceson")
    time.sleep(2)
    expiry_month_box.send_keys(12)
    time.sleep(2)
    expiry_year_box.send_keys(2025)
    time.sleep(2)
    cvv_box.send_keys(112)
    time.sleep(2)
    submit_btn.click()

    time.sleep(5)
    
    driver.quit()

    



# main
test_front_page()
# test_hotellist_card()
test_hotellist_select()
test_confirmation_page()