from tool.get_session import GetSession


class ApiPublishNotice:
    def api_publish_notice(self, url, id):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "publishone",
            "id": id

        }
        session = GetSession().get_session()
        return session.put(url, json=data, headers=headers)
