# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""
#11题
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&ch=14&tn=98012088_6_dg&wd=python&rsv_pq=82b5f33100005869&rsv_t=c188dHPqOCZlTmaCT1/11otuJOykdPX8XwTi2oQweSAMX8GI49Rgcj7W2r60eRFJ+YziQA&rqlang=cn&rsv_enter=1&rsv_sug3=4&rsv_sug1=5&rsv_sug7=101&rsv_sug2=1&prefixsug=py&rsp=0&inputT=5466&rsv_sug4=10175'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
ls1=re.compile('<div class="c-abstract">(.*?)</div>').findall(data)
ls2=re.compile('style="text-decoration:none;">(.*?)&nbsp').findall(data)
for i in range(8):
    print("标题:{}\n描述:{}\n网址:{}\n".format(ls[i+5],ls1[i],ls2[i]))
#12题
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"description":"(.*?)"').findall(data)
ls1=re.compile('"temp":(.*?)"').findall(data)
ls2=re.compile('"pressure":(.*?)"').findall(data)
for i in range(36):
    print("天气情况:{},温度:{},气压:{},".format(ls[i],ls1[i],ls2[i]))
    
#13题
import urllib.request as r
for a in range(1,14):
    req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
    myurl=r.urlopen(req)
    print(myurl.getcode())
    data=myurl.read().decode('utf-8')
    pat='<div class="content">(.*?)</div>'
    pat1='<h2>(.*?)</h2>'
    import re
    ls=re.compile(pat,re.S).findall(data)
    ls1=re.compile(pat1,re.S).findall(data)
    for i in range(25):
        print('作者:{}\n内容:{}'.format(ls1[i],ls[i]).replace('<span>','').replace('</span>',''))
    