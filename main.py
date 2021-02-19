from selenium import webdriver
import settings

browser = webdriver.Chrome()
browser.get('https://e-report.neu.edu.cn/mobile/notes/create')

username = browser.find_element_by_id('un')
password = browser.find_element_by_id('pd')

username.send_keys(settings.username)
password.send_keys(settings.password)

index_login_btn = browser.find_element_by_id('index_login_btn')
index_login_btn.click()



