import platform
import random
import string
import time
from configparser import ConfigParser


def load_prop_file(file_name):
    """ this method will read data from properties file
    if the properties file is under a directory you should give directory_name/file_name
    """
    config = ConfigParser()
    config.read(f"../{file_name}.properties")
    return config._sections


def get_system_os_type():
    """ this method will recognise the current os type and return the name of it"""
    os_name = platform.system()
    return os_name


def sleep_seconds(seconds):
    time.sleep(seconds)


def generate_string(upper=0, lower=0, number=0, special=0):
    """ this method will generate random string based on the given inputs"""
    lower = [random.choice(string.ascii_lowercase) for _ in range(lower)]
    upper = [random.choice(string.ascii_uppercase) for _ in range(upper)]
    number = [random.choice(string.digits) for _ in range(number)]
    special = [random.choice(string.punctuation) for _ in range(special)]

    final_string = number + special +  lower + upper
    return "".join(final_string)
