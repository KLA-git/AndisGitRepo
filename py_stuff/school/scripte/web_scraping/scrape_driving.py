
from selenium import webdriver
from config import username, password
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome("/Users/andi/Desktop/andisGitRepo/py_stuff/school/scripte/web_scraping/chromedriver")

response = driver.get("https://neilo.webuntis.com/WebUntis/?school=fvsg-fulda#/basic/login")

username_box = driver.find_elements_by_tag_name('input')[0]
password_box = driver.find_elements_by_tag_name('input')[1]

username_box.send_keys(username)
password_box.send_keys(password)

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.submit()


driver.get("https://neilo.webuntis.com/timetable-teachers-my/2021-03-28")

driver.close()





