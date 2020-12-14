from tool.get_session import GetSession


class ApiBanNotice:
    def api_ban_notice(self, url, id):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "banone",
            "id": id

        }
        session = GetSession().get_session()
        return session.put(url, json=data, headers=headers)
