from cmath import exp
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
import names
from random_word import RandomWords

letter_list= string.ascii_letters
char_list= string.ascii_letters + string.digits + string.punctuation # random string of characters
country_list= ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
# print(len(country_list))

def testing_input():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    print('driver Title:',driver.title)
    print('Driver name:',driver.name)
    print('Driver URL:',driver.current_url)

#generates valid dates but they may be wayy off
def generate_valid_date():
    rand_year= random.randint(2000, 2050)
    rand_month= random.randint(1, 12)
    rand_day= random.randint(1, 31)
    res= str(rand_year) + "-" + str(rand_month) + "-" + str(rand_day)
    return res

#generates a pair of dates that only differ by a bit
def generate_very_valid_date():
    rand_year= 2022
    rand_month1= random.randint(9, 12)
    
    rand_day1= random.randint(1, 31) # for checkin
    if(rand_day1>=30 and rand_month1==12):
        rand_day2= random.randint(1,31)
        rand_month2= 1
        rand_year= 2023

    elif(rand_day1>=30):
        rand_day2= random.randint(1,31)
        rand_month2= rand_month1 + 1
    else:
        rand_day2= random.randint(rand_day1+1, 31)
        rand_month2= random.randint(rand_month1, 12)

    checkin= str(rand_year) + "-" + str(rand_month1) + "-" + str(rand_day1)
    checkout= str(rand_year) + "-" + str(rand_month2) + "-" + str(rand_day2)
    return checkin, checkout

def generate_valid_country():
    return country_list[random.randint(0, 247)]

def generate_valid_rooms():
    return random.randint(1, 5)

def generate_valid_adults():
    return random.randint(1, 5)

def generate_valid_children():
    return random.randint(0, 5)


############# for use in confirmation page ################

def generate_valid_title():
    title_list= ["Mr.", "Ms.", "Mrs."]
    return title_list[random.randint(0,2)]

def generate_valid_firstname():
    g= random.choice(["female", "male"])
    res= names.get_first_name(gender=g)
    return res

def generate_valid_lastname():
    return names.get_last_name()

def generate_valid_fullname():
    return names.get_full_name()

def generate_valid_countrycode():
    res= "+"
    res+= str(random.randint(0,99))
    return res

def generate_valid_phonenumber():
    return random.randint(10000000, 9999999999)

def generate_longmessage():
    res= ""
    r= RandomWords().get_random_words()
    if(r!=None):
        for x in r:
            res+= x + " "
    else:
        res=""
    return res

def generate_valid_cardnumber():
    return random.randint(100000000, 999999999)

def generate_valid_month():
    return random.randint(1, 12)

def generate_valid_year():
    return random.randint(2023, 2030)

def generate_valid_CVV():
    return random.randint(100, 999)
    
# main
# print(generate_random())
# print(generate_valid_date())
# print(generate_valid_country())
# for x in range(20):
#     print(generate_very_valid_date())

# print(generate_valid_firstname())
# print(generate_valid_lastname())
# print(generate_longmessage())