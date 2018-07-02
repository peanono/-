# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:12:06 2018

=====================一定要注意文件格式，保存的时候为utf-8
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序

@author: Administrator
"""
print('火车站三字码是：'+'BJX')

"""
    ls=open('D:app/火车站编码.csv','r').readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xf8 in position 6572: illegal multibyte sequence
"""
def hanzi_to_pin(s):
    ls=open('D:app/火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc
###########第十题
import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
#print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data1=data['data']['result']

#p='  '
#s="v8hzesw92snv0p%2BXbBSYcvDvrkZJongII6gnHaa1K%2B5ZLSH2S1yiEmi5TocBRsVZ7KheRoWRj4s2%0AVRYp%2F1qQIXo6MxxZNB3giUuTVVn2qCjkK0zSOEIvJTiliIOKVW5rcQneIukZPdBmkyTOIosb%2FhFD%0AtpChpGqPNAY%2F29y3VTJO4Sh51LMePmFmF7Hv7THUyJDqN5VO5lYhnC611uP65vpluqQm243rAtJw%0AYiIa3SmEBr%2FXR331dZJkt7EmP3dw|预订|76000C630407|C6304|IXW|JFW|IVW|CNW|09:46|10:47|01:01|Y|NiY4S31uZETanTCgYyNeHA1zyfhqgCHmfzE%2B20yxLvYgcLOY|20180625|3|W1|02|06|1|0|||||||有||||无|无|||O0M0O0|OMO|0"
p='  '
#s=data[17]
#ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print('\n')
#车次   车发站，到达站 出发时间,到达时间 历时间
l=len(data1)
for j in range(l):
    ls=data1[j]
    ls=ls.split('|')
    ls[6]=data['data']['map'].get('{}'.format(ls[6]))
    ls[7]=data['data']['map'].get('{}'.format(ls[7]))
    ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--',ls[23],'--',ls[28],'--',ls[26],ls[29],'--',ls[1]]
    for i in ls:
        print(str(i).center(15).replace('[','').replace(']',''),end='')
    print('\n')

t=[]
for i in range(len(data1)):
    s=data1[i]
    ls=s.split('|')
    lp=ls[10]
    t.append(lp)
sorted(t)

t1=[]
for i in range(len(data1)):
    s=data1[i]
    ls=s.split('|')
    lp=ls[8]
    t1.append(lp)
sorted(t1)

l=len(ls)
for i in range(l):
    lp=ls[i][5]+' '+ls[i][0]
    t.append(lp)
sorted(t)



#print('车次')
#print('ab')


#将火车站三字码替换成城市名map{}






























