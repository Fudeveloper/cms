import requests
import json

post_data = {"username": "admin", "password": "admin"}
headers = {'User-Agent': 'webClient'}

API_ADDRESS = "http://120.78.62.39:8088"

# 登陆
res = requests.post(API_ADDRESS + "/Api/Account/Logon", json=post_data, headers=headers)
response_data = json.loads(res.text)['errorData']
print(res.text)
cookies = res.cookies
# print(cookies)
# print(res)
# 查询当前用户信息

# result = requests.get(API_ADDRESS + "/Api/Account/UserInfo", headers=headers).text
#
# data = json.loads(result)
# print(data)
# print(data['appendData']['groupID'])
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
# result = requests.put("http://120.78.62.39:8088/Api/Account/PassWordChange?id=9", json=data, headers=headers,cookies=cookies).text
#
# print(result)


# result = requests.get("http://120.78.62.39:8088/Api/Permiss/Info?userId=9",  headers=headers,cookies=cookies).text

# print(result)

# 查询某用户权限信息

# #
# result = requests.get(API_ADDRESS + "/Api/Permiss/GetData?userId=3", headers=headers, cookies=cookies).text
#
# result = json.loads(result)
#
# status = result['status']
# print(result)
# if status == 1:
#     appendData = result['appendData']
#     print(appendData)
# if "errorDat" in result.keys():
#     print(result['appendData'])

# if result['errorData'] == "获取权限成功":


# result = requests.get(API_ADDRESS + "/Api/Account/UserInfo?id=12", headers=headers).text
#
# result = json.loads(result)
# print(result)
# "无权限"
# result = requests.get("http://120.78.62.39:8088/Api/Account/UserInfoOnLoginList", headers=headers).text
# json_result = json.loads(result)
# # user_infos = json_result['appendData']
# print(json_result)

# result = requests.get(API_ADDRESS + "/Api/Login_Log/List?offset=0&limit=0", headers=headers, cookies=cookies).text
# print(cookies['CookiesName'])
# data = json.loads(result)
# print(data)
# print(data['appendData']['name'])

# result = requests.get(API_ADDRESS + "/Api/Device/List?offset=0&limit=0", headers=headers, cookies=cookies).text
# print(cookies['CookiesName'])
# data = json.loads(result)
# print(data)
# print(data['appendData']['name'])

# 操作设备
# data = {"deviceState": "0", "deviceID": "3"}
# result = requests.post(API_ADDRESS + "/Api/DeviceData/UpDataDevState", headers=headers, cookies=cookies, json=data).text
#
# print(result)
# data = {"id": "3"}
# result = requests.post(API_ADDRESS + "/Api/DeviceData/GetData", headers=headers, cookies=cookies, json=data).text
# result = json.loads(result)
#
# print(result['appendData'])
# headers = {
#     'User-Agent': 'webClient',
#     'content-type': 'text',  # 具体要什么的格式,自己拼接http头就行
#     'method': 'post'
# }
# 修改某用户权限
# data = [
#     {
#         "permissName": "alterUserPassword"
#     },
#     {
#         "permissName": "addUser"
#     },
#     {
#         "permissName": "alterUserPermiss"
#     }
# ]

# data = '[ {"permissName":"addUser"}]'
# data = ({"permissName": "addUser"})
# result = requests.put(API_ADDRESS + "/Api/Permiss/UpData?userId=10", headers=headers, cookies=cookies, json=data).text
#
# print(result)

# data = {"id": "3"}
# result = requests.post(API_ADDRESS + "/Api/DeviceData/List", headers=headers, cookies=cookies, json=data).text
# result = json.loads(result)
#
# device = result['appendData']
# for de in device:
#     print(de)
# 获取所有权限
# result = requests.get(API_ADDRESS + "/Api/Permiss/Get", headers=headers, cookies=cookies).text
#
# data = json.loads(result)
# datas = data['appendData']
# print(len(data))
# for data in datas :
#     print(data['permissName'])