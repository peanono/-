# -*- coding: utf-8 -*-
"""
Spyder Editor


This is a temporary script file.
"""

x=3
y='男'

##第一题
temp=[25,26,24,28,30,31,34]
print(temp[0])
print(temp[1])
print(temp[2])
print(temp[3])
print(temp[4])
print(temp[5])
print(temp[6])
print('星期三的温度是:'+str(temp[2])+'度')

##第二题
t={"温度":[16,15,20,21,22,23,24],"天气情况":['小雨','小雨','晴','晴','晴','晴','晴'],"最高温度":[20,21,22,30,25,36,30]}
t["温度"][2]
t["天气情况"][2]
t["最高温度"][2]


#第三题
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/weather?q=kunming&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data['description']['temp']['pressure']
print('昆明温度是:'+str(data['main']['temp']))
print('昆明气压是:'+str(data['main']['pressure']))
print('昆明天气情况是:'+str(data['weather'][0]['description']))

