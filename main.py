#! python3
# encoding:utf-8

from selenium import webdriver

info_file = open('./info.txt')
username = info_file.readline()[9:].strip()
password = info_file.readline()[9:].strip()

# browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser = webdriver.Edge(executable_path='./msedgedriver.exe')
browser.get('https://e-report.neu.edu.cn/mobile/notes/create')

username_input = browser.find_element_by_id('un')
password_input = browser.find_element_by_id('pd')

username_input.send_keys(username)
password_input.send_keys(password)

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
