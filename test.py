import os

import requests

import api
from config import BASE_PATH
from tool.get_session import GetSession

headers = {'Content-Type': 'application/json'}
data = {
    "action": "signin",
    "username": 'test01',
    "password": '123456'
}
data2 = {
    "action": "signin",
    "username": 'byhy',
    "password": '111111'
}
session = GetSession().get_session()
print(session.cookies)
re = session.post('http://127.0.0.1/api/sign',
                  json=data, headers=headers)
print('-' * 50)
print(session.cookies)
session.post('http://127.0.0.1/api/sign',
                  json=data2, headers=headers)
print('-' * 50)
print(session.cookies)
# with open(BASE_PATH + os.sep + 'data' + os.sep + '我的头像.jpg', 'rb') as f:
#     headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"}
#     file = {'upload1':f}
#     print(file)
#     r = session.post('http://127.0.0.1//api/upload',files=file)
#     print(r.json())
# params = {"action": "getmyprofile"}
# data = {
#             "action": "setmyprofile",
#             "newdata": {
#                 "realname": "test0101",
#                 "password": "123456"
#             }
#         }
# re = session.post(api.info_url,params=params,json=data,headers =headers)
# print(re.text)
# print(re.headers)
