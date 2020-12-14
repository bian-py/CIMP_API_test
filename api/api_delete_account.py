from tool.get_session import GetSession


class ApiDeleteAccount:
    def api_delete_account(self, url, id):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "deleteone",
            "id": id
        }
        session = GetSession().get_session()
        return session.delete(url, json=data, headers=headers)

