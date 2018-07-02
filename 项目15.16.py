# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:47:36 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法
@author: Administrator
"""

#题目15
class weather:
    #天气对象产生的时候，会调用这个方法weather()
    def __init__(self,temp,description,pre):#########系统固定的方法
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):#self 有对象
        print('天气属性是：温度是{},情况是{},气压是{}'.format(self.temp,self.description,self.pre))
a=weather('20','小雨','1600')
b=weather('25','晴','1200')
c=weather('24','晴','1400')
a.msg()
b.msg()
c.msg()
#题目16
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北','福建':'华东','江西':'华东','山东':'华东','上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','河南':'华中','湖北':'华中','湖南':'华中','广东':'华南','广西':'华南','海南':'华南','西藏':'华南','四川':'西南','贵州':'西南','云南':'西南','重庆':'西南','西藏':'西南','陕西':'西北','甘肃':'西北','青海':'西北','宁夏':'西北','新疆':'西北','北京':'华北','天津':'华北','山西':'华北','河北':'华北','内蒙古':'华北'}
areaplan={'东北':0,'华东':0,'华中':0,'华南':0,'西南':0,'西北':0,'华北':0}
z1=[]
import urllib.request as r
url='file:d:/app/全国招生计划表.txt'
data=r.urlopen(url).read().decode('utf-8')
data=data.split('\n')
import json
for i in range(len(data)):
    a=json.loads(data[i])
    z1.append(a)
    for w in range(len(z1)):
        if z1[w]['status']==0:
            continue
        ls=z1[w]['data']
        for school in ls:
           city=school['city']
           areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
a=areaplan['东北']+areaplan['华东']+areaplan['华中']+areaplan['华南']+areaplan['西南']+areaplan['西北']+areaplan['华北']
print('东北的招生人数是{}\n华东的招生人数是{}\'华中的招生人数是{}\n华南的招生人数是{}\n西南的招生人数是{}\n西北的招生人数是{}\n华北的招生人数是{}'.format(areaplan['东北']))

area={'黑龙江':'东北','吉林':'东北','辽宁':'东北','福建':'华东','江西':'华东','山东':'华东','上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','河南':'华中','湖北':'华中','湖南':'华中','广东':'华南','广西':'华南','海南':'华南','西藏':'西南','四川':'西南','贵州':'西南','云南':'西南','重庆':'西南','陕西':'西北','甘肃':'西北','青海':'西北','宁夏':'西北','新疆':'西北','北京':'华北','天津':'华北','山西':'华北','河北':'华北','内蒙古':'华北'}
areaplan={'东北':0,'华东':0,'华中':0,'华南':0,'西南':0,'西北':0,'华北':0}
sum=0
b={}
ls=[]
f=open('D:/APP/全国招生计划表.txt')
a=f.readlines()#将文本中的每行数据读入列表
import json
for i in range(len(a)):
    b[i]=json.loads(a[i])
for d in range(len(b)):
    if b[d]['status']==1:
        ls.append(b[d])
for e in range(59033):
    for g in range(len(ls[e]['data'])):
        city=ls[e]['data'][g]['city']
        areaplan[area[city]]=areaplan[area[city]]+int(ls[e]['data'][g]['plan'])
print('全国2300所学校：\n在东北的招生人数:{}\n在华东的招生人数：{}\n在华中的招生人数:{}\n在华南的招生人数:{}\n在西南的招生人数:{}\n在西北的招生人数:{}\n在华北的招生人数:{}'.format(areaplan['东北'],areaplan['华东'],areaplan['华中'],areaplan['华南'],areaplan['西南'],areaplan['西北'],areaplan['华北']))
