from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.51job.com')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_css_selector('.ush a[class="more"]').click()
driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_css_selector("[class='tit'] span").click()# 这边挡住了 需要点一下旁边
driver.find_element_by_id('work_position_input').click()
ele = driver.find_element_by_css_selector('em[class="on"]').text
if ele != '杭州':
    driver.find_element_by_css_selector('em[class="on"]').click()
    driver.find_element_by_css_selector('[data-value="080200"]').click()
    driver.find_element_by_id('work_position_click_bottom_save').click()
else:
    driver.find_element_by_id('work_position_click_bottom_save').click()
driver.find_element_by_css_selector("[class='tit'] span").click()# 这边挡住了 需要点一下旁边
driver.find_element_by_id('funtype_click').click()
driver.find_element_by_css_selector('em[data-value="0100"]').click()
driver.find_element_by_css_selector('[data-value="0106"][data-navigation="0100"]').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
driver.find_element_by_css_selector('#cottype_list span[class="ic i_arrow"]').click()
driver.find_element_by_css_selector('#cottype_list span[data-value="01"]').click()
driver.find_element_by_css_selector('#workyear_list span[class="ic i_arrow"]').click()
driver.find_element_by_css_selector('#workyear_list span[data-value="02"]').click()
driver.find_element_by_css_selector('[class="btnbox p_sou"] span[class="p_but"]').click()

eles = driver.find_elements_by_css_selector('#resultList div[class=el]')
for one in eles:
    log = one.find_elements_by_css_selector('span')
    lists = []
    for list in log:
        last = list.text
        lists.append(last)
    print(' | '.join(lists))  # 添加进一个列表里面print(' | '.join(lists))#添加进一个列表里面

driver.close()










# driver.find_element_by_css_selector("[id='work_position_input']").click()
# driver.find_element_by_css_selector('[data-value="070200"][data-navigation="000000"]').click()
# driver.find_element_by_css_selector('[data-value="080200"]').click()
# driver.find_element_by_css_selector('[class="p_but"]').click()
# driver.find_element_by_css_selector('.ush  button').click()
#
# eles = driver.find_elements_by_css_selector('#resultList div[class=el]')
# for one in eles:
#     log = one.find_elements_by_css_selector('span')
#     lists = []
#     for list in log:
#         stringFilelds = list.text
#         lists.append(stringFilelds)
#
#     print(' | '.join(lists))#添加进一个列表里面



