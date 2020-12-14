from tool.get_session import GetSession


class ApiSetInfo:
    def api_set_info(self, name ,url):
        headers = {'Content-Type': 'application/json'}
        params = {"action": "getmyprofile"}
        session = GetSession().get_session()
        data = {
            "action": "setmyprofile",
            "newdata": {
                "realname": name,
                "password": "123456"
            }
        }
        return session.post(url, json=data, params=params,headers=headers)
