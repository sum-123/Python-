# -*- encoding: utf-8 -*-
'''
@File : mp3.py
@Time : 2020/04/29 20:38:45
@Author : zjm 
@Version : 3.7.6
@Contact : 1005564803@qq.com
@WebSite : https://github.com/sum-123/Python-.git
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote
import os
def getHtmlText(url):
    try:        
        r = requests.get(url,timeout=30)   
        r.raise_for_status()       
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"
def fillList(ulist,txt,url):
     
    soup=BeautifulSoup(txt,'html.parser')
    Tags=soup.find_all('a')
    for tag in Tags:
         if '.mp3' in tag.string:
            ulist.append(url+quote(re.search(r'sc\-ad[\s\S]{1,100}\.mp3',tag.get('href')).group(0)))
    print(ulist)
def downloadmp3(ulist):
    for mp3 in ulist:
        os.system( 'wget ' + mp3 + ' ' + mp3.split('/')[-1] )

def main():
    mp3url_list=[]
    url='http://www.listeningexpress.com/studioclassroom/ad/'
    txt=getHtmlText(url)
    fillList(mp3url_list,txt,url)
    # downloadmp3(mp3url_list)
    # print(txt)
main()


