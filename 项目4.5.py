# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:54:17 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=kunming,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
#data['list'][0]['main']['temp']


t1=data['list'][1]['dt_txt']
a1=data['list'][1]['main']['temp']
a2=data['list'][1]['weather'][0]['main']
a3=data['list'][1]['main']['temp_max']
a4=data['list'][1]['main']['temp_min']
a5=data['list'][1]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t1,a1,a2,a3,a4,a5),'pay attention:today is cloudy,you should drink water,take the umbralla')
t2=data['list'][3]['dt_txt']
a1=data['list'][3]['main']['temp']
a2=data['list'][3]['weather'][0]['main']
a3=data['list'][3]['main']['temp_max']
a4=data['list'][3]['main']['temp_min']
a5=data['list'][3]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t2,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t3=data['list'][7]['dt_txt']
a1=data['list'][7]['main']['temp']
a2=data['list'][7]['weather'][0]['main']
a3=data['list'][7]['main']['temp_max']
a4=data['list'][7]['main']['temp_min']
a5=data['list'][7]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t3,a1,a2,a3,a4,a5),'pay attention:today is cloudy,you should drink water,take the umbralla')
t4=data['list'][9]['dt_txt']
a1=data['list'][9]['main']['temp']
a2=data['list'][9]['weather'][0]['main']
a3=data['list'][9]['main']['temp_max']
a4=data['list'][9]['main']['temp_min']
a5=data['list'][9]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t4,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t5=data['list'][11]['dt_txt']
a1=data['list'][11]['main']['temp']
a2=data['list'][11]['weather'][0]['main']
a3=data['list'][11]['main']['temp_max']
a4=data['list'][11]['main']['temp_min']
a5=data['list'][11]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t5,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t6=data['list'][15]['dt_txt']
a1=data['list'][15]['main']['temp']
a2=data['list'][15]['weather'][0]['main']
a3=data['list'][15]['main']['temp_max']
a4=data['list'][15]['main']['temp_min']
a5=data['list'][15]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t6,a1,a2,a3,a4,a5),'pay attention:today is cloudy,you should drink water,take the umbralla')
t7=data['list'][17]['dt_txt']
a1=data['list'][17]['main']['temp']
a2=data['list'][17]['weather'][0]['main']
a3=data['list'][17]['main']['temp_max']
a4=data['list'][17]['main']['temp_min']
a5=data['list'][17]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t7,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t8=data['list'][19]['dt_txt']
a1=data['list'][19]['main']['temp']
a2=data['list'][19]['weather'][0]['main']
a3=data['list'][19]['main']['temp_max']
a4=data['list'][19]['main']['temp_min']
a5=data['list'][19]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t8,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t9=data['list'][23]['dt_txt']
a1=data['list'][23]['main']['temp']
a2=data['list'][23]['weather'][0]['main']
a3=data['list'][23]['main']['temp_max']
a4=data['list'][23]['main']['temp_min']
a5=data['list'][23]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t9,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t10=data['list'][25]['dt_txt']
a1=data['list'][25]['main']['temp']
a2=data['list'][25]['weather'][0]['main']
a3=data['list'][25]['main']['temp_max']
a4=data['list'][25]['main']['temp_min']
a5=data['list'][25]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t10,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t11=data['list'][27]['dt_txt']
a1=data['list'][27]['main']['temp']
a2=data['list'][27]['weather'][0]['main']
a3=data['list'][27]['main']['temp_max']
a4=data['list'][27]['main']['temp_min']
a5=data['list'][27]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t11,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t12=data['list'][31]['dt_txt']
a1=data['list'][31]['main']['temp']
a2=data['list'][31]['weather'][0]['main']
a3=data['list'][31]['main']['temp_max']
a4=data['list'][31]['main']['temp_min']
a5=data['list'][31]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t12,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t13=data['list'][33]['dt_txt']
a1=data['list'][33]['main']['temp']
a2=data['list'][33]['weather'][0]['main']
a3=data['list'][33]['main']['temp_max']
a4=data['list'][33]['main']['temp_min']
a5=data['list'][33]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t13,a1,a2,a3,a4,a5),'pay attention:today is rainning,you should drink water,take the umbralla')
t14=data['list'][35]['dt_txt']
a1=data['list'][35]['main']['temp']
a2=data['list'][35]['weather'][0]['main']
a3=data['list'][35]['main']['temp_max']
a4=data['list'][35]['main']['temp_min']
a5=data['list'][35]['main']['pressure']
print('kunming{}的temp{}，description{}，max_temp{}，min_temp{}，pressure{}'.format(t14,a1,a2,a3,a4,a5))
if temp<20:
    print("穿长袖,注意保暖")
if temp>20:
    print("穿短袖")
    
temp1=data['list'][0]['main']['temp']
temp2=data['list'][8]['main']['temp']
temp3=data['list'][16]['main']['temp']
temp4=data['list'][24]['main']['temp']
temp5=data['list'][32]['main']['temp']
print(int(temp1)*'-')
print(int(temp2)*'-')
print(int(temp3)*'-')
print(int(temp4)*'-')
print(int(temp5)*'-')

ls=[]
ls.append(22.06)
ls.append(17.43)
ls.append(23.96)
ls.append(23.18)
ls.append(16.08)
ls.append(23.95)
ls.append(18.84)
ls.append(16.63)
ls.append(24.2)
ls.append(17.46)
sorted(ls)

def time(i):
    time=data['list'][i]['dt_txt']
    return time
def a (i):
    a=data['list'][i]['main']['temp']
    return a
def b (i):
    b=data['list'][i]['weather'][0]['main']
    return b
def c (i):
    c=data['list'][i]['main']['pressure']
    return c
def d (i):
    d=data['list'][i]['main']['temp_max']
    return d
def e (i):
    e=data['list'][i]['main']['temp_min']
    return e
print(int(temp1)*'-')
print(int(temp2)*'-')
print(int(temp3)*'-')
print(int(temp4)*'-')
print(int(temp5)*'-')
def msg(time,a,b,c,d,e):
    print('时间：{},温度：{},天气情况：{},气压：{},最高气温：{},最低气温：{}'.format(time,a,b,c,d,e))
msg(time(0),a(0),b(0),c(0),d(0),e(0))
msg(time(1),a(1),b(1),c(1),d(1),e(1))
msg(time(3),a(3),b(3),c(3),d(3),e(3))
msg(time(8),a(8),b(8),c(8),d(8),e(8))
msg(time(9),a(9),b(9),c(9),d(9),e(9))
msg(time(11),a(11),b(11),c(11),d(11),e(11))
msg(time(16),a(16),b(16),c(16),d(16),e(16))
msg(time(17),a(17),b(17),c(17),d(17),e(17))
msg(time(19),a(19),b(19),c(19),d(19),e(19))
msg(time(24),a(24),b(24),c(24),d(24),e(24))
msg(time(25),a(25),b(25),c(25),d(25),e(25))
msg(time(27),a(27),b(27),c(27),d(27),e(27))
msg(time(32),a(32),b(32),c(32),d(32),e(32))
msg(time(33),a(33),b(33),c(33),d(33),e(33))
msg(time(35),a(35),b(35),c(35),d(35),e(35))
print(int(a(0))*'-')
print(int(a(1))*'-')
print(int(a(3))*'-')
print(int(a(8))*'-')
print(int(a(9))*'-')
print(int(a(11))*'-')
print(int(a(16))*'-')
print(int(a(17))*'-')
print(int(a(19))*'-')
print(int(a(24))*'-')
print(int(a(25))*'-')
print(int(a(27))*'-')
print(int(a(32))*'-')
print(int(a(33))*'-')
print(int(a(35))*'-')