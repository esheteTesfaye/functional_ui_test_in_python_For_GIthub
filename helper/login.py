from helper.utils import load_xpath

login_xp = load_xpath("login")
email_xp = login_xp["login"]["email"]
password_xp = login_xp["login"]["password"]
submit_xp = login_xp["login"]["submit"]


