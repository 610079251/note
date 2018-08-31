# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:53:21 2018

@author: Administrator
"""

from selenium import webdriver


# 使用Selenium打开firefox浏览器
driver = webdriver.Firefox()
# 跳转到Bing首页
#driver.get("http://cn.bing.com/")
#driver.find_element_by_id('sb_form_q').send_keys("Python爬虫")
#driver.find_element_by_id('sb_form_go').click()
#print(driver.page_source)

driver.get("http://fanyi.youdao.com/")
driver.find_element_by_id('inputOriginal').send_keys("Spider")

# 关闭浏览器
#driver.quit() #关闭当前的Tab页
#driver.close()#通知浏览器关闭



