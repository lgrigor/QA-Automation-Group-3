import random
from string import ascii_letters, digits, punctuation

class TestData():

    #Drivers
    CHROME_PATH = r'CHROME_PATH_TO_DRIVER'
    FIREFOX_PATH = r'FIREFOX_PATH_TO_DRIVER'
    
    #Data
    VALID_EMAIL = 'test@gmail.com'
    VALID_PASSWORD = '^&*tESt123!@#'
    
    INVALID_EMAIL = 'testgmail.com'
    INVALID_PASSWORD = 'invalidpassword'

    RANDOM_EMAIL = ''.join(random.choices(ascii_letters + digits, k=10)) + '@gmail.com'
    RANDOM_PASSWORD = ''.join(random.choices(ascii_letters + digits + punctuation, k=16))