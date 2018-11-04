from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element_by_id('fromStationText')
ele.click()
ele.send_keys('南京南\n')
ele2 = driver.find_element_by_id('toStationText')
ele2.click()
ele2.send_keys('杭州东\n')

ele3 = Select(driver.find_element_by_id('cc_start_time'))
ele3.select_by_visible_text('06:00--12:00')
driver.find_element_by_css_selector('#date_range  li:nth-child(2)').click()
# 方法二：用css实现获取二等座有票的车次信息
print('\n\n\n===============================\n\n\n')
theTrainLines = driver.find_elements_by_css_selector('#queryLeftTable > tr')
# 先不加这个，发现特别慢
driver.implicitly_wait(0)
for one in theTrainLines:
    secondlevelseat = one.find_elements_by_css_selector('td:nth-of-type(4)[class]')
    if secondlevelseat:
        print (one.find_element_by_css_selector('td:nth-of-type(1) a').text)
driver.implicitly_wait(10)


driver.quit()
