# -*- coding:utf-8 -*-
 
import requests
import re
import time
 
# 把id替换成你想爬的地址id
urls = 'https://weibo.cn/comment/HmmkNjIzw?uid=1618051664&rl=1&page={}'
 
headers = {'Cookie' : 'MLOGIN=1; SCF=AmtQTWmFaTq6pbUo3HFUCpLfx59sDPJzeXiXtmS8SU9b-VDGdy9RiDlE7-3Jy2r72_6Qm3tdqFYkgjAAsmHuvmM.; M_WEIBOCN_PARAMS=luicode%3D20000174; SUB=_2A25xqOyaDeRhGeBP7lIR9ivKzjiIHXVTUvTSrDV6PUJbkdAKLWHMkW1NRV2LoA0eJeatYgaSv8dkjAJr9uLkTxPr; SUHB=0G0uLykt6vU1-A; WEIBOCN_FROM=deleted; _T_WM=3690fc6ed59470d9edae4370b50e3ee5',
           'User-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
}
# 找到html标签
tags = re.compile('</?\w+[^>]*>')
 
# 设置提取评论function
def get_comment(url):
    j = requests.get(url, headers=headers).json()
    comment_data = j['data']['data']
    for data in comment_data:
        try:
            comment = tags.sub('', data['text']) # 去掉html标签
            reply = tags.sub('', data['reply_text'])
            weibo_id = data['id']
            reply_id = data['reply_id']
            comments.append(comment)
            comments.append(reply)
            ids.append(weibo_id)
            ids.append(reply_id)
        except KeyError:
            pass

comments, ids = [], []
for i in range(1, 101):
    url = urls.format(str(i))
    get_comment(url)
    time.sleep(1) # 防止爬得太快被封
 
'''# 这里我用pandas写入csv文件，需要设置encoding，不然会出现乱码
df = pd.DataFrame({'ID': ids, '评论': comments})
df = df.drop_duplicates()
df.to_csv('观察者网.csv', index=False, encoding='gb18030')
'''
