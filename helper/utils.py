import platform
from configparser import ConfigParser

def load_xpath(file_name):
    """ this method will read data from properties file"""
    config = ConfigParser()
    config.read(f"../xpath/{file_name}.properties")
    return config._sections


def get_system_os_type():
    """ this method will recognise the current os type and return the name of it"""
    os_name = platform.system()
    return os_name
