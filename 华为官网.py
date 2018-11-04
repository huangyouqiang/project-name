# coding=utf-8
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get('https://www.vmall.com/')
til = driver.current_window_handle

driver.find_element_by_css_selector("div.s-sub a[href*='consumer.huawei']").click()
driver.switch_to_window(til)


driver.find_element_by_css_selector("body > div.shortcut > div > div.s-sub > ul > li:nth-child(11) > div > div.h > a").click()


driver.find_element_by_css_selector("a[href*='appstore.huawei.com']").click()


def checkHuawei():
    expected = '智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'


    eles = driver.find_elements_by_css_selector('[class="clearfix nav-cnt"]')
    eleTexts = [ele.text.replace('\n','|') for ele in eles]
    actual = '|'.join(eleTexts)
    print(eleTexts)
    if actual == expected:
        print('huawei page pass')
    else:
        print('huawei page fail!!!!')


def checkAppmarket():
    expected = u'''首页|游戏|软件|专题|品牌专区|华为软件专区'''

    eles = driver.find_elements_by_css_selector("ul.ul-nav   li")
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('app page pass')
    else:
        print('app page fail!!!!')


def checkVmall():
    expected = u'''平板电脑|笔记本电脑|笔记本配件'''
    from selenium.webdriver.common.action_chains import ActionChains
    ac = ActionChains(driver)
    ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

    eles = driver.find_elements_by_css_selector('#zxnav_1 li.subcate-item')
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('main page pass')
    else:
        print('main page fail!!!!')


mainWindow = driver.current_window_handle

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '消费者业务官网' in driver.title:
        checkHuawei()
    elif '应用市场' in driver.title:
        checkAppmarket()
    elif '商城官网' in driver.title:
        checkVmall()

driver.switch_to.window(mainWindow)
checkVmall()


driver.quit()