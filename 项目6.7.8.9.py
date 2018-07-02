# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""
##############第六题
import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E4%B9%90%E9%AB%98&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180622&ie=utf8&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
data['mods']['itemlist']['data']['auctions'][0]['raw_title']
for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][i]['nick']
    e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    print('商品名称：{},商品价格：{},付款人数：{},店铺名：{}，地址：{}'.format(a,b,c,d,e))
print('销量排序：')
ls=[]
for i in range(36):
    s=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    x=s.replace('人付款','')
    ls.append(int(x))
sorted(ls)
ls1=sorted(ls,reverse=True)
print(ls1)
        
for j in range(0,36):
     a=data['mods']['itemlist']['data']['auctions'][j]['raw_title']
     b=data['mods']['itemlist']['data']['auctions'][j]['view_fee']
     if b=='0.00':
         print(a,'包邮')
     else:
         print(a,'不包邮')
         
for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    try:
        f=data['mods']['itemlist']['data']['auctions'][i]['icon'][0]['iconPopupComplex']['subIcons'][0]
        ['icon_content']
        
    except Exception as err:
        if(f=='15天退货'):
            print('商品名称{},提供{}'.format(a,f))
            
            
            
###########第七题
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=kunming,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
#data['list'][0]['main']['temp']
for i in ("欢","迎","收","看","天","气","预","报"):
    print("&&&***╰(￣▽￣)╮",i,"╭(′▽`)╯***&&&")
    print("!☀ !☆ ! ☀!☆ ! ☀! ☆! ☀! ☆!")
    
for i in range(0,36):
    n=data['city']['name']
    t=data['list'][i]['dt_txt']
    desc=data['list'][i]['weather'][0]['description']
    if desc=='多云':
        print(n,t,desc,"好好玩耍，可以洗衣服，涂防晒霜")
    elif desc=='小雨':
        print(n,t,desc,"记得带伞，注意保暖")
    elif desc=='中雨':
        print(n,t,desc,"记得带伞，多喝热水，不要洗衣服")
        
        
########第八题 保存淘宝数据，小组项目
import urllib.request as r#导入联网工具包，命令为r
f=open('D:app/cyh.csv','w')#csv表格文件，以逗号分割
for i in range(100):
    url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180625&ie=utf8&loc=%E7%A6%8F%E5%BB%BA&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s={}&ajax=true'.format(i*44)
    data=r.urlopen(url).read().decode('utf-8')
    #讲str类型转换为dict
    import json
    data=json.loads(data)
    for i in range(len(data['mods']['itemlist']['data']['auctions'])):
        a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][i]['nick']
        d=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
        f.write("{},{},{},{},{}\n".format(a,b,c,d,e))        
f.close()#关闭文件，保存文件
        
        
############第九题
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-30&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']

p='  '
s="v8hzesw92snv0p%2BXbBSYcvDvrkZJongII6gnHaa1K%2B5ZLSH2S1yiEmi5TocBRsVZ7KheRoWRj4s2%0AVRYp%2F1qQIXo6MxxZNB3giUuTVVn2qCjkK0zSOEIvJTiliIOKVW5rcQneIukZPdBmkyTOIosb%2FhFD%0AtpChpGqPNAY%2F29y3VTJO4Sh51LMePmFmF7Hv7THUyJDqN5VO5lYhnC611uP65vpluqQm243rAtJw%0AYiIa3SmEBr%2FXR331dZJkt7EmP3dw|预订|76000C630407|C6304|IXW|JFW|IVW|CNW|09:46|10:47|01:01|Y|NiY4S31uZETanTCgYyNeHA1zyfhqgCHmfzE%2B20yxLvYgcLOY|20180625|3|W1|02|06|1|0|||||||有||||无|无|||O0M0O0|OMO|0"
p='  '
s=data[21]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')
        
             
    




