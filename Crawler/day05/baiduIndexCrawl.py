# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 09:24:10 2018

@author: Administrator
"""
from selenium import webdriver
import time

# 使用Selenium+浏览器来抓取百度指数
browser = webdriver.Firefox()
#第一步：打开浏览器，比如Firefox;
browser.get("http://index.baidu.com/#/")
#第二步: 登录百度指数；
browser.find_element_by_xpath('//*[@id="home"]/div[1]/div[2]/div[1]/div[4]/span/span').click()
time.sleep(3)
#TANGRAM__PSP_4__userName
browser.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('zhangsan')
#TANGRAM__PSP_4__password
browser.find_element_by_id('TANGRAM__PSP_4__password').send_keys('1234')
#TANGRAM__PSP_4__submit
browser.find_element_by_id('TANGRAM__PSP_4__submit').click()

#第三步: 进行搜索
# 清空网页输入框
browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div/div[2]/form/input[3]").clear()
# 写入需要搜索的百度指数
browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div/div[2]/form/input[3]").send_keys("Python")
browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div/div[2]/div/span").click()
time.sleep(2)
#第四步：滚动并且截图
browser.execute_script("window.scrollTo(0,1000)") # 执行滚屏操作
browser.save_screenshot("baiduIndex.png")         # 由于这里图片数据无法直接抓取，所以先截图保存

#第五步：尝试关闭浏览器
browser.close()
browser.quit()
