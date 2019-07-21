# -*- coding:utf-8 -*-


from selenium import webdriver
import time
driver = webdriver.Chrome()
url='https://www.baidu.com/'
driver.get(url)
time.sleep(3)


'''
保证跳转到最新网页
'''
while True:
    handles=driver.window_handles
    flag=False
    for handle in handles[::-1]:
        driver.switch_to.window(handle)
        if driver.title == u"百度一下，你就知道":
            flag=True
            print u'百度一下，你就挂了'
            break
    if flag:
        break

driver.close()













