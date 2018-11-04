from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.51job.com')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_css_selector("[id='kwdselectid']").send_keys('python')
driver.find_element_by_css_selector("[id='work_position_input']").click()
driver.find_element_by_css_selector('[data-value="070200"][data-navigation="000000"]').click()
driver.find_element_by_css_selector('[data-value="080200"]').click()
driver.find_element_by_css_selector('[class="p_but"]').click()
driver.find_element_by_css_selector('.ush  button').click()

eles = driver.find_elements_by_css_selector('#resultList div[class=el]')
for one in eles:
    log = one.find_elements_by_css_selector('span')
    lists = []
    for list in log:
        stringFilelds = list.text
        lists.append(stringFilelds)

    print(' | '.join(lists))#添加进一个列表里面



