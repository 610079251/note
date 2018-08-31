# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:48:24 2018

@author: Administrator
"""

import builtwith
# 用这个parse来检测当前这个网站使用了什么技术
#print(builtwith.parse("http://www.sina.com.cn"))
print(builtwith.parse("http://www.sohu.com"))

import whois
#print(whois.whois("http://www.sina.com.cn"))
#{
#  "domain_name": "sina.com.cn",
#  "registrar": "\u5317\u4eac\u65b0\u7f51\u6570\u7801\u4fe1\u606f\u6280\u672f\u6709\u9650\u516c\u53f8",
#  "whois_server": null,
#  "referral_url": null,
#  "updated_date": null,
#  "creation_date": null,
#  "expiration_date": null,
#  "name_servers": [
#    "ns1.sina.com.cn",
#    "ns2.sina.com.cn",
#    "ns3.sina.com.cn",
#    "ns4.sina.com.cn"
#  ],
#  "status": [
#    "clientDeleteProhibited",
#    "serverDeleteProhibited",
#    "clientUpdateProhibited",
#    "serverUpdateProhibited",
#    "clientTransferProhibited",
#    "serverTransferProhibited"
#  ],
#  "emails": "domainname@staff.sina.com.cn",
#  "dnssec": "unsigned",
#  "name": null,
#  "org": null,
#  "address": null,
#  "city": null,
#  "state": null,
#  "zipcode": null,
#  "country": null
#}
print(whois.whois("http://www.baidu.com"))
#{
#  "domain_name": [
#    "BAIDU.COM",
#    "baidu.com"
#  ],
#  "registrar": "MarkMonitor, Inc.",
#  "whois_server": "whois.markmonitor.com",
#  "referral_url": null,
#  "updated_date": [
#    "2017-07-28 02:36:28",
#    "2017-07-27 19:36:28"
#  ],
#  "creation_date": [
#    "1999-10-11 11:05:17",
#    "1999-10-11 04:05:17"
#  ],
#  "expiration_date": [
#    "2026-10-11 11:05:17",
#    "2026-10-11 00:00:00"
#  ],
#  "name_servers": [
#    "DNS.BAIDU.COM",
#    "NS2.BAIDU.COM",
#    "NS3.BAIDU.COM",
#    "NS4.BAIDU.COM",
#    "NS7.BAIDU.COM",
#    "dns.baidu.com",
#    "ns4.baidu.com",
#    "ns7.baidu.com",
#    "ns2.baidu.com",
#    "ns3.baidu.com"
#  ],
#  "status": [
#    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
#    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
#    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
#    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
#    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
#    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
#    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
#    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
#    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
#    "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
#    "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
#    "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
#  ],
#  "emails": [
#    "abusecomplaints@markmonitor.com",
#    "whoisrelay@markmonitor.com"
#  ],
#  "dnssec": "unsigned",
#  "name": null,
#  "org": "Beijing Baidu Netcom Science Technology Co., Ltd.",
#  "address": null,
#  "city": null,
#  "state": "Beijing",
#  "zipcode": null,
#  "country": "CN"
#}