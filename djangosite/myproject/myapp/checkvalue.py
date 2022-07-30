## check title, country code, card number, expiredate, cvv
import phonenumbers
from datetime import datetime
title_space = ["Mr. ","Ms. ", "Mrs. "]

def check_title(inputval):
    if inputval not in title_space:
        return False
    else:
        return True
#print(check_title("Mr."))


def check_phonenumber(PhoneNumber):
    
    phone_number = phonenumbers.parse(PhoneNumber)

     # Validating a phone number

    valid = phonenumbers.is_valid_number(phone_number)

    return valid
#print(check_phonenumber("+658467210"))
def check_cvv(cvv):
    if cvv.isnumeric() and (len(cvv) == 3 or len(cvv) == 4):
        return True
    else:
        return False
#print(check_cvv("845"))
def check_cardnumber(cardnumber):
    if cardnumber.isnumeric() and len(cardnumber) <=19:
        return True
    else:
        return False

def check_expire(year,month):
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    if int(year) < int(currentYear):
        return False
    elif int(year) == int(currentYear) and int(month) < int(currentMonth):
        return False
    else:
        return True
#print(check_expire('2022','6'))

def check_not_empty(input):
    if input != '':
        return True
    else:
        return False

