import os

# 文件路径配置信息
BASE_PATH = os.path.dirname(__file__)
# print(BASE_PATH,os.path)

# 数据库连接配置信息
db = {
    'db1':
    {'host': '192.168.1.10',
     'user': 'root',
     'password': 'root',
     'database': 'hmtt',
     'port': 3306,
     }
}
# 手机连接配置信息
cap = {
  "platformName": "Android",
  "platformVersion": "6",
  "deviceName": "emulator-5554",
  "appPackage": "com.android.settings",
  "appActivity": ".Settings",
  "newCommandTimeout": 600
}
# 主机配置
cap2 = \
{
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "HJS0218B27006432",
  "appPackage": "com.android.settings",
  "appActivity": ".Settings",
  "newCommandTimeout": 600
}
cap3 = {
  "platformName": "Android",
  "platformVersion": "5.1",
  "deviceName": "192.168.19.101:5555",
  "appPackage": "com.android.settings",
  "appActivity": ".Settings",
  "newCommandTimeout": 600
  # "automationName":"UiAutomator1"

}