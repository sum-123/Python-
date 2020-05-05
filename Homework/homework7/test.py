# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/04/30 15:19:30
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
# import requests
#******亚马逊网站爬取*******
# url='https://www.amazon.cn/dp/B01N6Y63QU/ref=sr_1_6?__mk_zh_CN=亚马逊网站&crid=MQ0AJCYVM20I&keywords=手机&qid=1588319759&sprefix=shoji%2Caps%2C165&sr=8-6'
# try:
#     kv={'User-agent':'Mozilla/5.0'}
#     r=requests.get(url,headers = kv)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text)
# except:
#     print('爬取失败')

# print(r.request.headers)
# print(r.encoding)
# print(r.apparent_encoding)
# print(r.status_code)
# print(r.encoding)
# print(r.text)
#**************百度360搜索关键词提交*****************
# keyword='meinv'
# try:
#     kv1={'User-agent':'Mozilla/5.0'}
#     kv={'wd':keyword}
#     r=requests.get('http://www.baidu.com/s',params=kv,headers=kv1)
#     print(r.request.headers)
#     print(r.request.url)
#     r.raise_for_status()
#     print(r.text)
# except:
#     print('爬取失败')
# ************图片爬取*********************
# import os
# url=''
# root='/Users/zhaojiaming/Desktop/'
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r=requests.get(url)
#         with open(path,'wb') as f:
#             f.write(r.content)
#             f.close()
#             print('文件保存成功')
#     else:
#         print('文件已存在')
# except:
#     print('爬取失败')
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(open('/Users/zhaojiaming/Desktop/index.html'),'html.parser')
# print(soup.a.parent.parent.parent.parent.name)
# print(soup.a.attrs)
# print(type(soup.a.attrs))
# print(type(soup.a))
# for child in soup.body.children:
#     print(child)
#     print('*'*10)
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# for sibling in soup.body.next_siblings:
#     print(sibling)
#     print('*'*10)
# print(soup.prettify())
# try:
#     r=requests.get('https://www.9x600.com')
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     demo=r.text
#     soup=BeautifulSoup(demo,'html.parser')
#     for link in soup.find_all('a'):
#         print(link.get('href'))
# except:
#     print('False')
# import requests
# from bs4 import BeautifulSoup
# import bs4
# def getHTMLText(url):
# 	try:
# 		r=requests.get(url,timeout=30)
# 		r.raise_for_status()
# 		r.encoding=r.apparent_encoding
# 		return r.text
# 	except:
# 		return ''

# def fillUnivList(ulist,html):
# 	soup=BeautifulSoup(html,'html.parser')
# 	for tr in soup.find('tbody').children:
# 		if isinstance(tr,bs4.element.Tag):
# 			tds=tr('td')
# 			ulist.append([tds[0].string,tds[1].string])
            
# def printList(uList,num):
# 	print('{:^10}\t{:^6}\t{:^10}'.format('12','34','56'))
# 	for i in range(num):
# 		u=uList[i]
# 		# print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))
   
# def main():
#     uinfo=[]
#     url = 'http://www.gaokao.com/e/20200325/5e7aecd42f074.shtml' 
#     html = getHTMLText(url)
#     fillUnivList(uinfo,html)
#     # printList(uinfo,20)
#     print(uinfo,20)
# main()
import requests
from bs4 import BeautifulSoup
import bs4
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout = 30) 
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding 
#         return r.text
#     except: return ""
# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser") 
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[2].string])
# def printUnivList(ulist, num):
#     tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}" 
#     print(tplt.format("排名", "学校名称", "总分", chr(12288))) 
#     for i in range(num):
#         u = ulist[i]
#         print(tplt.format(u[0], u[1], u[2],chr(12288)))
# def main(): 
#     uinfo = []
#     url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html' 
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     # print(uinfo)
#     printUnivList(uinfo, 300) # 20 univs
# main()
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
# import wget
import os

url = 'http://www.listeningexpress.com/studioclassroom/ad/'
mp3_urls = []

pattern = r'sc\-ad[\s\S]{1,100}\.mp3'

home_page = requests.get( url )
page_text = home_page.text
soup = BeautifulSoup( page_text, 'html.parser' )

# print( page_text )
atags = soup.find_all( 'a' )
for atag in atags:
    if '.mp3' in atag.string:
        mp3_urls.append( url + quote( re.search( pattern, atag.get( 'href' ) ).group(0) ) )

# print( mp3_urls )
for mp3 in mp3_urls:
    # wget.download( mp3, mp3.split('/')[-1] )
    os.system( 'wget ' + mp3 + ' ' + mp3.split('/')[-1] )






