import requests

post_data = {"username": "admin", "password": "admin"}
import json

# post_data = json.dumps(post_data, ensure_ascii=False,)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
           # 'Content-Type': 'application/json '
           }
# import json
# res = requests.post("http://120.78.62.39:8088/Api/Account/Logon", json=post_data, headers=headers)
# response_data = json.loads(res.text)['errorData']
#
# print(response_data)

result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfo/",  headers=headers).content.decode('utf-8')

data = json.loads(result)
print(data['errorData'])


