# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 16:19:36 2018

@author: Administrator
"""
#import basicSpider
#import re
#
#crawled_queue = []#记录已爬URL的队列
#crawl_queue = []
#
#def CrawlInfo(seed_url):
#    # 处理一页数据
#    headers = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")]
#    html = basicSpider.downloadHtml(seed_url, headers=headers)
#    # 提取真正想要的数据
#    
#    
##    # 用正则匹配URL的翻页
##    pattern = re.compile('"https://www.douban.com/doulist/3516235/\?start=.*?"')
##    itemUrls = re.findall(pattern, html)
##    
##    # 用队列去模拟广度优先遍历
##    global crawled_queue#记录已爬URL的队列
##    global crawl_queue
##    for itemUrl in itemUrls:
##        #第一步去重：通过已爬队列信息来防止重复
##        if itemUrl not in crawled_queue:
##            crawl_queue.append(itemUrl)
##    #第二步去重：保证待爬队列本身不重复
##    crawl_queue = list(set(crawl_queue))
##    
##    # 模拟广度优先遍历的操作,直到这个crawl_queue为空，
##    #爬虫的逻辑才结束
##    while crawl_queue:
##        url = crawl_queue.pop(0)
##        CrawlInfo(url)
##        # 已爬队列应该只进不出
##        crawled_queue.append(url)
##    
##    # 保存到本地文件
##    return html
#
#if __name__ == "__main__":  
#    # 处理入口URL信息
#    seed_url = "https://www.douban.com/doulist/3516235/?start=0&sort=seq&sub_type="
#    # 抓取这页的数据
#    html = CrawlInfo(seed_url)
#
#    # 用正则匹配URL的翻页
#    pattern = re.compile('"https://www.douban.com/doulist/3516235/\?start=.*?"')
#    itemUrls = re.findall(pattern, html)
#    
#    # 用队列去模拟广度优先遍历
#    global crawled_queue#记录已爬URL的队列
#    global crawl_queue
#    for itemUrl in itemUrls:
#        #第一步去重：通过已爬队列信息来防止重复
#        if itemUrl not in crawled_queue:
#            crawl_queue.append(itemUrl)
#    #第二步去重：保证待爬队列本身不重复
#    crawl_queue = list(set(crawl_queue))
#    
#    # 模拟广度优先遍历的操作,直到这个crawl_queue为空，
#    #爬虫的逻辑才结束
#    while crawl_queue:
#        url = crawl_queue.pop(0)
#        CrawlInfo(url)
#        # 已爬队列应该只进不出
#        crawled_queue.append(url)
#    
#    # 保存到本地文件
#    return html   

from bs4 import BeautifulSoup
import re
import basicSpider

def get_html(url):
    """
    获取一页的网页源码信息
    """
    headers = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")]
    #proxy = {"http":"182.129.243.84:9000"}
    html = basicSpider.downloadHtml(url, headers=headers)
    return html

def get_movie_all(html):
    """
    获取当前页面中所有的电影的列表信息
    """
    soup = BeautifulSoup(html, "html.parser")
    movie_list = soup.find_all('div', class_='bd doulist-subject')
    #print(movie_list)
    return movie_list

def get_movie_one(movie):
    """
    获取一部电影的精细信息，最终拼成一个大的字符串
    """
    result = ""
    soup = BeautifulSoup(str(movie),"html.parser")
    title = soup.find_all('div', class_="title")
    soup_title = BeautifulSoup(str(title[0]), "html.parser")
    for line in soup_title.stripped_strings:
        result += line
    
    try:
        score = soup.find_all('span', class_='rating_nums')
        score_ = BeautifulSoup(str(score[0]), "html.parser")
        for line in score_.stripped_strings:
            result += "|| 评分："
            result += line
    except:
         result += "|| 评分：5.0"
         
    abstract = soup.find_all('div', class_='abstract')
    abstract_info = BeautifulSoup(str(abstract[0]), "html.parser")
    for line in abstract_info.stripped_strings:
        result += "|| "
        result += line    
    
    result += '\n'
    #print(result)
    return result

def save_file(movieInfo):
    """
    写文件的操作,这里使用的追加的方式来写文件
    """
    with open("doubanMovie.txt","ab") as f:
        f.write(movieInfo.encode("utf-8"))

def CrawlMovieInfo(url):
    """
    抓取电影一页数据，并写入文件
    """
    global crawl_queue
    global crawled_queue
    html = get_html(url)#获取当前的页面
    # 提取页面的URL链接
    pattern = re.compile('(https://www.douban.com/doulist/3516235/\?start=.*)"')
    itemUrls = re.findall(pattern, html)

    for item in itemUrls:
        if item not in crawled_queue: 
            # 第一步去重，确定这些url不在已爬队列中
            crawl_queue.append(item)
    #第二步去重，对待爬队列去重
    crawl_queue = list(set(crawl_queue))
    
    # 处理当前页面的数据，保存到文件系统中
    movie_list = get_movie_all(html)
    for it in movie_list:
        save_file(get_movie_one(it))
    
    crawled_queue.append(url)

# 两步去重操作
crawl_queue = []    # 待爬队列
crawled_queue = []  # 已爬取队列

if __name__ == "__main__":
    # 设置种子URL入队列
    seed_url = "https://www.douban.com/doulist/3516235/?start=0&amp;sort=seq&amp;sub_type="
    crawl_queue.append(seed_url)    
    # 模拟广度优先遍历
    # 说明：其实这个广度优先遍历原来的顺序在这里已经被打乱了
    while crawl_queue: #去待爬队列中取值，直到待爬队列为空
        url = crawl_queue.pop(0)#取出待爬队列中第一个值
        CrawlMovieInfo(url)