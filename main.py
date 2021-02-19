from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import settings

browser = webdriver.Chrome()
browser.get('https://e-report.neu.edu.cn/mobile/notes/create')

username = browser.find_element_by_id('un')
password = browser.find_element_by_id('pd')

username.send_keys(settings.username)
password.send_keys(settings.password)

index_login_btn = browser.find_element_by_id('index_login_btn')
index_login_btn.click()

try:
    by_yourself_spin = browser.find_elements_by_class_name('el-radio__inner')[0]
    by_yourself_spin.click()

    health_state_spin = browser.find_elements_by_class_name('el-radio__inner')[4]
    health_state_spin.click()

    journey_info_spin = browser.find_elements_by_class_name('el-radio__inner')[12]
    journey_info_spin.click()

    submit_btn = browser.find_elements_by_tag_name('button')[1]
    submit_btn.click()

    browser.find_elements_by_tag_name('img')[0]
finally:
    browser.close()
    browser.quit()
