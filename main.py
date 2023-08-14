import requests
import json
import random
import time
from datetime import datetime

url = "https://luntan.jishangkj.cn/api/wxPostv2/newPost"

# 打开文件并读取行
with open('text.txt', 'a+') as f:
    f.seek(0)
    content = f.readlines()

# 获取当前时间戳
current_timestamp = int(time.time())

# 将时间戳格式化为原格式的日期时间字符串
current_datetime = datetime.utcfromtimestamp(current_timestamp).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

headers = {
    # ... 省略 ...
}

data = {
    "xuanshang": False,
    "xs_medias": "[]",
    "target": 0,
    "chatgpt": 0,
    "pContent": content[random.randint(0, 1)],
    "pToId": 0,
    "pCreateTime": current_datetime,
    "pLastVisitTime": current_datetime,
    "pLastCommentTime": current_datetime,
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
