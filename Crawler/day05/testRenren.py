# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:54:50 2018

@author: Administrator
"""

#Cookie: anonymid=jkrz42tgrkfsh3; depovince=BJ; jebecookies=2f198e35-3532-46b2-b876-e3be8de78d04|||||; _r01_=1; JSESSIONID=abc4i56rT7sNx8twZpYuw; ick_login=7431f53e-ab61-44d4-a230-9833d2a74415; _de=7113E26C6AAF3646A83FD76533146E3C; p=74a053d1bae8188a68a823b4ebc1d2709; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=0bde19c8ceb46c3516c2786d5093a64f9; societyguester=0bde19c8ceb46c3516c2786d5093a64f9; id=961482489; xnsid=cdba3418; loginfrom=syshome; jebe_key=daa39ada-a364-4e93-8b90-b1317e37a888%7C65617699d9107c4fa92a82edbc369e2a%7C1534146761728%7C1%7C1534146622310; wp_fold=0

import urllib
url = "http://www.renren.com/961482489/profile"
# 使用cookie来完成人人网的登录过程，但是这个cookie需要首先登录才能拿到。
#而且这个cookie时效性的。
ua_headers={"Connection":"keep-alive",
            "Cookie":"anonymid=jkrz42tgrkfsh3; depovince=BJ; jebecookies=2f198e35-3532-46b2-b876-e3be8de78d04|||||; _r01_=1; JSESSIONID=abc4i56rT7sNx8twZpYuw; ick_login=7431f53e-ab61-44d4-a230-9833d2a74415; _de=7113E26C6AAF3646A83FD76533146E3C; p=74a053d1bae8188a68a823b4ebc1d2709; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=0bde19c8ceb46c3516c2786d5093a64f9; societyguester=0bde19c8ceb46c3516c2786d5093a64f9; id=961482489; xnsid=cdba3418; loginfrom=syshome; jebe_key=daa39ada-a364-4e93-8b90-b1317e37a888%7C65617699d9107c4fa92a82edbc369e2a%7C1534146761728%7C1%7C1534146622310; wp_fold=0",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Host":"www.renren.com"
            }
# 发起请求
req = urllib.request.Request(url, headers=ua_headers)
response = urllib.request.urlopen(req)
with open("myRenren.html", "wb") as f:
    f.write(response.read())



