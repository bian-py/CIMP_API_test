from tool.get_session import GetSession


class ApiModifyNotice:
    def api_modify_account(self, url, id, title):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "modifyone",
            "id": id,
            "newdata": {
                "title": title
            }
        }
        session = GetSession().get_session()
        return session.put(url, json=data, headers=headers)
