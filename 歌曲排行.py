# 打开百度新歌榜， http: // music.baidu.com / top / new

# 在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者
#
# 注意： 有的歌曲名里面有
# "影视原声"
# 这样的标签， 要去掉




from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://music.baidu.com/top/new')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_css_selector("[class='enter pa']").click()
driver.find_element_by_css_selector("[class='close-vip-app']").click()


total = int(driver.find_element_by_css_selector('.PNNW-S:nth-child(3)').text)
print(total)
i = 1
index = 0
while i<= total:
    eles = driver.find_elements_by_css_selector('#songListWrapper li')
    for ele in eles:
        songName = ele.find_element_by_css_selector('[data-film="null"]').text
        singer = ele.find_element_by_css_selector('[class="author_list"]').text
        # upTags = ele.find_elements_by_class_name("up")       #这样写 问题很大   会运行很慢
        # if upTags:
        classValue = ele.find_element_by_tag_name('i').get_attribute('class')== 'up'#  应该这样写
        if classValue :
            print('{0:{2}<24}:{1:}'.format(songName, singer, chr(12288)))
            index +=1

    if i == total:
        break
    driver.find_element_by_css_selector('.page-navigator-next').click()
    i +=1
print('一共有{}首歌曲'.format(index))
driver.quit()

#
#
#
#
# index=0
# next = driver.find_element_by_css_selector('.page-navigator-next')
# while next:
#
#     driver.implicitly_wait(10)
#     ele = driver.find_elements_by_css_selector('.song-item')
#
#     for one in ele:
#         uptarge = one.find_elements_by_css_selector('.up')
#         if uptarge:
#             titleStr = one.find_element_by_class_name("song-title").find_element_by_css_selector('[data-film="null"]').text
#
#
#             authorsStr = one.find_element_by_class_name("author_list").text
#             index+=1
#
#
#
#             print('{:10s}:{}'.format(titleStr, authorsStr))
#
# print('一共有{}首歌曲'.format(index))
#
# driver.quit()
#
#
#
#










# driver.quit()