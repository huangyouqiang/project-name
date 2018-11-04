from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://tinypng.com/')
driver.implicitly_wait(10)
driver.find_element_by_css_selector('figure.icon').click()
time.sleep(2)

#直接发松键盘信息给当前程序
#前提是浏览器必须是当前应用

import win32com.client
shell = win32com.client.Dispatch('WScript.shell')
shell.Sendkeys(r"G:\DSC_193880.jpg" + '\n')
