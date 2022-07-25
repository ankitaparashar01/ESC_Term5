from cryptography.fernet import Fernet
def generating_key():

    key = Fernet.generate_key()
    return key


def encryption(input_string, key):

    fernet = Fernet(key)
    encMessage = fernet.encrypt(input_string.encode())

    return encMessage

def decryption(enc, key):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(enc).decode()

    return decMessage

def mask(number):
    masked = number[:6] + len(number[5:-4])*"#"+number[-4:]
    return masked




