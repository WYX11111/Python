# -*- coding:utf-8 -*-

import requests
import re
import time
def get_one_page(url):#请求函数：获取某一网页上的所有内容
    headers = {
    'User-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
    'Host' : 'weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie' : 'MLOGIN=1; SCF=AmtQTWmFaTq6pbUo3HFUCpLfx59sDPJzeXiXtmS8SU9b-VDGdy9RiDlE7-3Jy2r72_6Qm3tdqFYkgjAAsmHuvmM.; M_WEIBOCN_PARAMS=luicode%3D20000174; SUB=_2A25xqOyaDeRhGeBP7lIR9ivKzjiIHXVTUvTSrDV6PUJbkdAKLWHMkW1NRV2LoA0eJeatYgaSv8dkjAJr9uLkTxPr; SUHB=0G0uLykt6vU1-A; WEIBOCN_FROM=deleted; _T_WM=3690fc6ed59470d9edae4370b50e3ee5',
    'DNT' : '1',
    'Connection' : 'keep-alive'
     }#请求头的书写，包括User-agent,Cookie等
    response = requests.get(url,headers = headers,verify=False)#利用requests.get命令获取网页html
    if response.status_code == 200:#状态为200即为爬取成功
        return response.text#返回值为html文档，传入到解析函数当中
    return None
def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    with open('test.txt','a',encoding='utf-8') as fp:
        fp.write(result)

for i in range(28412):
    url = "https://weibo.cn/comment/HmmkNjIzw?uid=1618051664&rl=1&page="+str(i)
    html = get_one_page(url)
    print(html)
    print('正在爬取第 %d 页评论' % (i+1))
    parse_one_page(html)
    time.sleep(3)
