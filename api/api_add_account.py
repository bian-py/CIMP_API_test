from tool.get_session import GetSession


class ApiAddAccount:
    def api_add_account_post(self, url, realname, username, password, number, desc, type):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "addone",
            "data": {
                "realname": realname,
                "username": username,
                "password": password,
                "studentno": number,
                "desc": desc,
                "usertype": type
            }
        }
        session = GetSession().get_session()
        return session.post(url, json=data, headers=headers)
