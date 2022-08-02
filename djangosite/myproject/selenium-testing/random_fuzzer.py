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

letter_list= string.ascii_letters
# print(len(letter_list))
char_list= string.ascii_letters + string.digits + string.punctuation # random string of characters

def testing_input():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)


def generate_random():
    res= ""
    iter= random.randint(3,30)
    for x in range(iter):
        res+= char_list[random.randint(0, 93)]
    return res

def generate_random_date1():
    rand_year= random.randint(0, 9999)
    rand_month= random.randint(0, 99)
    rand_day= random.randint(0, 99)
    res= str(rand_year) + "-" + str(rand_month) + "-" + str(rand_day)
    return res

def generate_random_country():
    res = ""
    iter= random.randint(3,20)
    for x in range(iter):
        res+= letter_list[random.randint(0, 51)]
    return res



# main
# print(generate_random())
# print(generate_random_date1())
# print(generate_random_country())