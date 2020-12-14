from tool.get_session import GetSession


class ApiModifyAccount:
    def api_modify_account(self, url, id, realname):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "modifyone",
            "id": id,
            "newdata": {
                "realname": realname,
            }
        }
        session = GetSession().get_session()
        return session.put(url, json=data, headers=headers)
