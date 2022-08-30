import time
import requests
import numpy
# import detect
from detect import *

# 填写对应的喵码


id = 'tjXvHO4'
# 填写喵提醒中，发送的消息，这里放上前面提到的图片外链
ts = str(time.time())  # 时间戳
type = 'json'  # 返回内容格式
request_url = "http://miaotixing.com/trigger?"
# count = count
# 获取detect.py统计人数的值
for c in count:
    c = c.cuda().data.cpu().numpy()
    print(c)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}

    text = "人头计数：" + "http://rhdbeqgut.hn-bkt.clouddn.com/head_test.jpg" + "\n" + "总人数:" + str(c)

    result = requests.post(
        url=request_url + "id=" + id + "&text=" + text + "&ts=" + ts + "&type=" + type,
        headers=headers,
    )
    print(result)
