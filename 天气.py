# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
#
# ele = driver.find_element_by_id("forecastID")
# print(ele.text)
# weather = ele.text
# lowweather = weather.repalce('℃','')
# print(lowweather)
# driver.close()

from selenium import webdriver
driver = webdriver.Chrome()

# ------------------------
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_css_selector("#forecastID")#用ID定位


''' 
citysWeather是每个城市的温度信息 list

每个元素像这样：
南京
12℃/27
'''

citysWeather = ele.text.split('℃\n')


# 算出温度最低城市

lowest = 100
lowestCity = []  # 温度最低城市列表
for one in citysWeather:
    one = one.replace('℃','')
    print(one)
    parts = one.split('\n')
    curcity =parts[0]


    lowweather = min([int(one) for one in parts[1].split('/')])#列表生成式
    lowweather = int(lowweather)
    #发现气温更低的城市
    if lowweather<lowest:
        lowest = lowweather
        lowestCity = [curcity]
    #  温度和当前最低相同，加入列表
    elif lowweather ==lowest:
        lowestCity.append(curcity)
#


print('温度最低为{}℃, 城市有{}'.format(lowest, lowestCity))
# ------------------------

driver.quit()
