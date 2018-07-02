# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:10:48 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""
import urllib.request as r
url='file:///d:/app/all_school.txt'
d=r.urlopen(url).read().decode('utf-8')
print(d)
import re
ls=re.compile('jianjie-(.*?).html').findall(d)
ls1=re.compile('(.*?)http://').findall(d)
for i in range(2300):
    print('学校地区:{} 编号:{}'.format(ls1[i],ls[i]))
    
import urllib.request as r
url='http://www.gaokaopai.com/daxue-zhaosheng-924.html'
data='id=924&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import re
ls1=re.compile('<li data-val=(.*?)data-id="2"').findall(d)
ls2=re.compile("'claimCity',(.*?)\S\S>").findall(d)
for i in range(31):
    print('城市:{} 编号:{}'.format(ls1[i],ls2[i]))
    
f=open('./a.txt','w')
f=write(b+"\n")
f.close()



########
f=open('./gd.txt','w')
ls=[]
import urllib.request as r
for i in ls:
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=44&state=1'.format(i).encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        ls.append(d)
        f.write('{}\n'.format(d))
        print('{}ok'.format(i))
f.close()

for j in range(2300):
    a=ls[j]
    if a.startwith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=44&state=1'.format(ls[j])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d2=r.urlopen(req).read().decode('utf-8','ignore')
        ls[i]=d2
        
#修改后重新写入数据.txt
f=open('./数据.txt','w',encoding='utf-8')
for i in range(0,2300):
    b=ls[j]
    f.write(b+"\n")
f.close()
####################
import urllib.request as r
for i in ls:
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=44&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    if d[0]=='{':
        f=open('./gdw.txt','a')
        f.write('{}\n'.format(d))
        f.close()
        print(i)
    else:
        while d[0]!='{':
            url='http://www.gaokaopai.com/university-ajaxGetMajor.html' 
            data='id={}&type=1&city=44&state=1'.format(i).encode()
            req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
            d=r.urlopen(req).read().decode('utf-8','ignore')
        f=open('./gdw.txt','a')
        f.write('{}\n'.format(d))
        f.close()
























