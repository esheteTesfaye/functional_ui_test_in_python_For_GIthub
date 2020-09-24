from configparser import ConfigParser

def load_xpath(file_name):
    """ this method will read data from properties file"""
    config = ConfigParser()
    config.read(f"../xpath/{file_name}.properties")
    return config._sections
