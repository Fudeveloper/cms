import requests
import json

post_data = {"username": "admin", "password": "admin"}
headers = {'User-Agent': 'webClient'}
API_ADDRESS = "http://120.78.62.39:8088"

# 登陆
res = requests.post(API_ADDRESS + "/Api/Account/Logon", json=post_data, headers=headers)
response_data = json.loads(res.text)['errorData']
# print(res.text)
print(res.cookies)
cookies = res.cookies
# print(res)
# 查询当前用户信息

# result = requests.get(API_ADDRESS + "/Api/Account/UserInfo", headers=headers).text
#
# data = json.loads(result)
# print(data)
# print(data['appendData']['name'])
# 从服务器获取所有用户信息
# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfoList", headers=headers).text
# json_result = json.loads(result)
# user_infos = json_result['appendData']
# print(json_result)
#
# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfo?id=", headers=headers).text
# json_result = json.loads(result)
# user_infos = json_result['appendData']
# print(user_infos)


# 修改任意用户密码
# data = {"passWordOld": "null", "passWordNew": "123"}
# result = requests.put("http://120.78.62.39:8088/Api/Account/PassWordChange?id=9", json=data, headers=headers).text
#
# print(result)


# result = requests.get("http://120.78.62.39:8088/Api/Permiss/Info?userId=9",  headers=headers).text

# print(result)

# 查询某用户权限信息

#
# result = requests.get(API_ADDRESS + "/Api/Permiss/GetData?userId=12", headers=headers).text
#
# result = json.loads(result)
# # status = result['status']
# # if status == 1:
# #     appendData = result['appendData']
# # print(appendData)
# print(result)

# result = requests.get(API_ADDRESS + "/Api/Account/UserInfo?id=12", headers=headers).text
#
# result = json.loads(result)
# print(result)
# "无权限"
# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfoOnLoginList", headers=headers).text
# json_result = json.loads(result)
# # user_infos = json_result['appendData']
# print(json_result)

result = requests.get(API_ADDRESS + "/Api/Login_Log/List?offset=0&limit=0", headers=headers, cookies=cookies).text
print(cookies['CookiesName'])
data = json.loads(result)
print(data)
# print(data['appendData']['name'])
