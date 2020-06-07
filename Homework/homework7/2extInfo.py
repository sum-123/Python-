# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/04/27 16:41:06
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
    给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
'''

# here put the import lib
import re
from bs4 import BeautifulSoup
import requests

keywords = [ '企业介绍', '关于我们', '企业发展', '发展历史', '企业概况' ]

urls = [] # links of home page of the companies
intro_urls = [] # introduction of the companies
pattern = r'http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

with open( 'webspiderUrl.txt', 'r' ) as f:
    content = f.readlines()
    for line in content:
        urls += re.findall( pattern, line )


error_cnt = 0
with open( 'hw2_errorurl.txt', 'w' ) as error_file:

    for url in urls:
        try:
            home_page = requests.get( url )
        except requests.exceptions.ConnectionError:
            print( '连接失败' %url )
            error_file.write( url )
            error_file.write( '   ' )
            error_cnt += 1
            if error_cnt % 5 == 0:
                f.write( '\n' )

        page_text = home_page.text # get the html text

        soup = BeautifulSoup( page_text, 'html.parser' )
        atag = soup.find_all( 'a' ) # find tag 'a'
        for tag in atag:
            if tag.string in keywords:
                if 'http://' not in tag.get( 'href' ):
                    intro_url = url + '/' + tag.get( 'href' )
                else:
                    intro_url = tag.get( 'href' )
                if intro_url not in intro_urls:
                        intro_urls.append( intro_url )


cnt = 0
with open( 'hw2_com_intro.txt', 'w' ) as f:
    for intro_url in intro_urls:
        f.write( intro_url )
        f.write( '   ' )
        cnt += 1
        if cnt % 5 == 0:
            f.write( '\n' )
