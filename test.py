import requests

post_data = {"username": "lalala", "password": "lalala"}
import json

# post_data = json.dumps(post_data, ensure_ascii=False,)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
           # 'Content-Type': 'application/json '
           }
import json

# 登陆
res = requests.post("http://120.78.62.39:8088/Api/Account/Logon", json=post_data, headers=headers)
response_data = json.loads(res.text)['errorData']
print(response_data)

# 查询当前用户信息
# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfo/",  headers=headers).text
#
# data = json.loads(result)

# # 从服务器获取所有用户信息
# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfoList", headers=headers).text
# json_result = json.loads(result)
# user_infos = json_result['appendData']
# print(user_infos)

# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfo?id=", headers=headers).text
# json_result = json.loads(result)
# user_infos = json_result['appendData']
# print(user_infos)



data = {"passWordOld": "null", "passWordNew": "123"}
result = requests.put("http://120.78.62.39:8088/Api/Account/PassWordChange?id=9", json=data, headers=headers).content

print(result)
