import platform
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
