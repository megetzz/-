import requests
import MyUserAgent
import random
from bs4 import BeautifulSoup
import os

url='https://pvp.qq.com/web201605/herolist.shtml'
headers={
    'User-Agent':random.choice(MyUserAgent.my_chorme_agent)
}
proxies={'http': '123.169.162.230:9999'}

res=requests.get(url,headers=headers,proxies=proxies)
res.encoding=res.apparent_encoding
# print(res.text)
soup=BeautifulSoup(res.text,'html.parser')
herolist=soup.select('body > div.wrapper > div > div > div.herolist-box > div.herolist-content > ul >li >a ')
# herolist=soup.select('')
# print(herolist)
# body > div.wrapper > div > div > div.herolist-box > div.herolist-content > ul > li:nth-child(1)
for i in herolist:
    j=i.img
    # print(j)
    src_1=j.get('src')
    alt_1=j.get('alt')
    new_name = alt_1+'.jpg'
    new_url = 'http:'+src_1
    print(new_url)
    with open(new_name,'wb')as f:
        f.write(requests.get(new_url).content)
