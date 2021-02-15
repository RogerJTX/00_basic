 1 import requests
 2 import json
 3
 4 def getDingMes():
 5
 6     baseUrl = " your hook address。"
 7
 8     # please set charset= utf-8
 9     HEADERS = {
10         "Content-Type": "application/json ;charset=utf-8 "
11     }
12
13 # 这里的message是你想要推送的文字消息
14     message = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
15     stringBody ={
16         "msgtype": "text",
17         "text": {"content": message},
18         "at": {
19             "atMobiles": ["1825718XXXX"],
20                "isAtAll": True   #@所有人 时为true，上面的atMobiles就失效了
21         }
22  }
23     MessageBody = json.dumps(stringBody)
24     result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
25     print(result.text)
26
27 if __name__ == '__main__':
28     getDingMes()