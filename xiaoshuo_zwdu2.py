# -*- coding:utf-8 -*-
#测试用压缩的数据
import re,random
from typing import List
from urllib.request import Request, urlopen
import gzip,zlib,time
import json,tkinter,turtle
from bs4 import BeautifulSoup

#www.booktxt.net顶点小说网

#小说章节调用
def xiaoshuo_zj(url,xiaoshuo_name):
   # 构建请求
   # 包装头部
   firefox_headers = {
       'User-Agent': "	Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0 ",
       "Accept-Encoding": "gzip, deflate"}
   # 构建请求
   request = Request(url, headers=firefox_headers)
   html = urlopen(request)

   # 获取数据以gbk的编码方式
   # data2 = html.read().decode('utf-8')
   data2 = zlib.decompress(html.read(), 16 + zlib.MAX_WBITS).decode('gbk')
   xiaoshuo = BeautifulSoup(data2, 'html5lib')

   # xiaoshuo2=json.loads(data2)
   xiaoshuo_zhangjie_name0 = xiaoshuo.find_all(class_='bookname')
   xiaoshuo_txt0 = xiaoshuo.find_all(id="content")

   # 去除HTML标签
   dr = re.compile(r'<[^>]+>', re.S)
   xiaoshuo_zhangjie_name = dr.sub('', str(xiaoshuo_zhangjie_name0))

   xiaoshuo_txt = dr.sub('', str(xiaoshuo_txt0))
   xiaoshuo_all = str(xiaoshuo_zhangjie_name) + '\n' + str(xiaoshuo_txt) + '\n' + '\n'

   f = open(xiaoshuo_name+'.txt', 'a+',encoding='utf8')
   f.write(xiaoshuo_all)
   f.close()



#网站获取小说目录
print('请输入小说的目录地址，仅限于www.zwdu.com。类似https://www.zwdu.com/book/33376/ \n 网址:')
url=input()
#url = 'https://www.zwdu.com/book/33376/'
#包装头部
firefox_headers = {'User-Agent': "	Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0 " ,
                   "Accept-Encoding" :"gzip, deflate"}

#构建请求

request = Request( url, headers=firefox_headers )
html = urlopen( request )

#获取数据以gbk的编码方式
data2 = zlib.decompress(html.read(), 16+zlib.MAX_WBITS).decode('gbk')
#data1=str(data2)



#去除HTML标签
dr = re.compile(r'<[^>]+>' ,re.S)
xiaoshuo = BeautifulSoup(data2,'html5lib')

xiaoshuo_name0 =xiaoshuo.h1
#去除HTML标签
dr = re.compile(r'<[^>]+>',re.S)
xiaoshuo_name = dr.sub('',str(xiaoshuo_name0))
#xiaoshuo_name1 = dr.sub('',str(xiaoshuo_name0))
print(xiaoshuo_name)


xiaoshuo_zhangjie= xiaoshuo.find_all('dd')
xiaoshuo_zhangjie0 = dr.sub('',str(xiaoshuo_zhangjie))
#xiaoshuo_zhangjie=xiaoshuo.find_all('dd',class_ = 'col-md-3')
#xiaoshuo_zhangjie0=re.findall(r'href="(.*?)">(.*?)<',xiaoshuo_zhangjie)

#print(xiaoshuo_zhangjie0)
#对章节名称及链接进行再次解析
zhangjie_name=[]
zhangjie_url=[]
x=0


f = open(str(xiaoshuo_name + '.txt'), 'a+',encoding="utf-8")
f.write(xiaoshuo_name+'\n'+url+'\n'+'\n')
f.close()
#print('0')

 #获取每一章的链接并提取name和url
for i in xiaoshuo.findAll('dd'):
    for j in i.children:
        zhangjie_name.append(j.text)
        zhangjie_url.append('http://www.zwdu.com'+j.get("href"))
		#zhangjie_url.append('http://www.zwdu.com'+'/'+j.get("href"))
#打印测试证明章节名以及链接正确

print('请输入小说开始的章节 \n')
t_start=input()
for k in range(int(t_start),(len(zhangjie_name)),1):
#    xiaoshuo_zj(zhangjie_url[k], xiaoshuo_name)
    print(str(k)+str(zhangjie_name[k]))
    print(str(zhangjie_url[k]))
    time.sleep(random.random()*1.02+1.21+random.random()*0.71)
    xiaoshuo_zj(zhangjie_url[k], xiaoshuo_name)
'''
for k in range(0,(len(zhangjie_name)),1):
#   xiaoshuo_zj(zhangjie_url[k],xiaoshuo_name)
   print(str(zhangjie_name[k]))
   print(str(zhangjie_url[k]))
'''
