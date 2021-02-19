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

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'index_login_btn'))
    )
    index_login_btn = browser.find_element_by_id('index_login_btn')
    index_login_btn.click()

    by_yourself_spin = browser.find_elements_by_name('jibenxinxi_shifoubenrenshangbao')[0]
    by_yourself_spin.click()

    health_state_spin = browser.find_elements_by_name('jiankangxinxi_muqianshentizhuangkuang')[0]
    health_state_spin.click()

    journey_info_spin = browser.find_elements_by_id('xingchengxinxi_weizhishifouyoubianhua')[0]
    journey_info_spin.click()

    submit_btn = browser.find_element_by_class_name('el-button Findbutton el-button--primary')
    submit_btn.click()
finally:
    browser.close()
    browser.quit()
