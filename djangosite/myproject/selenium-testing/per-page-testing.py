from cmath import exp
from email import message
from traceback import print_stack
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
    time.sleep(1)
    search_hotel_btn= driver.find_element(By.NAME, "submitButton")
    search_hotel_box= driver.find_element(By.NAME, "destinationorhotel")
    checkin_box= driver.find_element(By.NAME, "checkin")
    checkout_box= driver.find_element(By.NAME, "checkout")
    room_box= driver.find_element(By.NAME, "roomsnumber")
    adult_box= driver.find_element(By.NAME, "adultsnumber")
    children_box= driver.find_element(By.NAME, "childrennumber")

    search_hotel_box.send_keys("Rome")
    time.sleep(2)
    search_hotel_box.send_keys(Keys.DOWN)
    search_hotel_box.send_keys(Keys.ENTER)

    time.sleep(1)
    checkin_box.send_keys(Keys.ENTER)
    checkout_box.send_keys(Keys.ENTER)
    room_box.send_keys(3)
    adult_box.send_keys(2)
    time.sleep(1)
    children_box.send_keys(2)
    time.sleep(1)
    search_hotel_btn.click()
    time.sleep(2)
    driver.quit()

def test_hotellist_card():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    # driver.get("http://127.0.0.1:8000/hotellistings/dest_id=A6Dz")
    driver.get("http://127.0.0.1:8000/hotellistings/?destinationorhotel=Rome%2C+Italy&checkin=Thursday%2C25+August%2C2022&checkout=Monday%2C+29+August%2C+2022&roomsnumber=1&adultsnumber=1&childrennumber=0&submitButton=")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    # driver.implicitly_wait(5)
    time.sleep(1)
    # for now not implemented yet
    search_hotel_btn= driver.find_element(By.NAME, "submitButton")
    search_hotel_box= driver.find_element(By.NAME, "destinationorhotel")
    checkin_box= driver.find_element(By.NAME, "checkin")
    checkout_box= driver.find_element(By.NAME, "checkout")
    room_box= driver.find_element(By.NAME, "roomsnumber")
    adult_box= driver.find_element(By.NAME, "adultsnumber")
    children_box= driver.find_element(By.NAME, "childrennumber")

    search_hotel_box.send_keys("Singapore")
    checkin_box.send_keys(Keys.ENTER)
    checkout_box.send_keys(Keys.ENTER)
    room_box.send_keys(3)
    adult_box.send_keys(2)
    children_box.send_keys(4)
    time.sleep(1)
    driver.quit()
    
def test_hotellist_select():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/hotellistings/?destinationorhotel=Rome%2C+Italy&checkin=Thursday%2C25+August%2C2022&checkout=Monday%2C+29+August%2C+2022&roomsnumber=1&adultsnumber=1&childrennumber=0&submitButton=")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)
    time.sleep(2)
    # driver.implicitly_wait(5)
    see_details_btn= driver.find_element(By.NAME, "seeDetailsButton")

    see_details_btn.click()

    time.sleep(2)
    driver.quit()


def test_confirmation_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/confirmation/dest_id=A6Dz/hotelName=Hotel%20Flavio%20Rome/hotelId=SPpa/roomKey=er-62AA84B7D5438C9F876DA1425B3D13C8-2EBF69C32423F4280F3FFB35267C8C32/roomType=200462189/checkin=Thursday,25%20August,2022/checkout=Monday,%2029%20August,%202022/guests=1/price=1067.82")
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
    first_name_box.send_keys("Bob")
    last_name_box.send_keys("Aliceson")
    country_code_box.send_keys("+65")
    phone_no_box.send_keys(84055585)
    message_box.send_keys("Clean up the room thoroughly, I am allergic to dust.")
    card_no_box.send_keys(1293281893913)
    name_card_box.send_keys("Bob Aliceson")
    expiry_month_box.send_keys(12)
    expiry_year_box.send_keys(2025)
    cvv_box.send_keys(112)
    time.sleep(2)
    submit_btn.click()
    time.sleep(2)

    driver.switch_to.alert.accept()
    time.sleep(2)

    
    driver.quit()

    

def test_front_page2():
    try:
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
        search_hotel_box.send_keys("Sing")
        time.sleep(3)
        search_hotel_box.send_keys(Keys.DOWN)
        time.sleep(1)
        search_hotel_box.send_keys(Keys.ENTER)

        time.sleep(2)
        checkin_box.send_keys("2022-08-07")
        time.sleep(2)
        checkout_box.send_keys("2022-08-10")
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

    except:
        print("Fail")
        print_stack()

# main
def main_function():
    test_front_page()
    test_hotellist_select()
    test_confirmation_page()

main_function()