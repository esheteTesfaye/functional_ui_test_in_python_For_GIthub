from helper.utils import load_xpath

login_xpath = load_xpath("login")
xpath_email = login_xpath["login"]["email"]
xpath_password = login_xpath["login"]["password"]
xpath_submit = login_xpath["login"]["submit"]