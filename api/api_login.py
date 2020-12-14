from tool.get_session import GetSession


class ApiLogin:

    def api_login_post(self, url, username, password):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "signin",
            "username": username,
            "password": password
        }
        session = GetSession.get_session()
        return session.post(url, json=data, headers=headers)

if __name__ == '__main__':
    re = ApiLogin().api_login_post(url='http://127.0.0.1//api/sign',username='byhy',password='111111')
    print(re.url)
    print(re.status_code)
    print(re.text)
    print(re.json())
    print(re.headers, type(re.headers))