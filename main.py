import requests
import json
import random
url = "https://luntan.jishangkj.cn/api/wxPostv2/newPost"
# 打开文件并读取行
# 使用 'w' 模式打开文件进行写入
with open('text.txt', 'a+') as f:
    f.seek(0)
    content=f.readlines()
# 现在，'lines'是一个列表，其中每个元素都是txt文件的一行。
with open('time.txt', 'a+') as f:
    f.seek(0)
headers = {
    "accept": "*/*",
    "content-type": "application/json; charset=UTF-8",
    "referer": "https://servicewechat.com/wx9ddd73d26fdbacba/152/page-frame.html",
    "x-token": "x-token",
    "token": "46619988-d41d-43d2-aba9-e8bc78b63cfd1687751819",
    "accept-language": "zh-CN,zh-Hans;q=0.9",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
    "accept-encoding": "gzip, deflate, br"
}

data = {
    "xuanshang": False,
    "xs_medias": "[]",
    "target": 0,
    "chatgpt": 0,
    "pContent": content[random.randint(0,1)],
    "pToId": 0,
    "pCreateTime": "2023-06-26T04:07:55.547Z",
    "pLastVisitTime": "2023-06-26T04:07:55.547Z",
    "pLastCommentTime": "2023-06-26T04:07:55.547Z",
    "pIsTop": 0,
    "tagarrs": "",
    "medias": "[]",
    "recordlist": [],
    "wxQR": [],
    "pContactStatus": 0
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.text)