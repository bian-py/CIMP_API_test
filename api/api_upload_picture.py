import os

from config import BASE_PATH
from tool.get_session import GetSession


class ApiUpload:
    def api_upload(self, url):
        with open(BASE_PATH + os.sep + 'data' + os.sep + '我的头像.jpg', 'rb') as f:
            headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"}
            file = {'upload1': f}
            session = GetSession().get_session()
            return session.post(url, files=file)
