from tool.get_session import GetSession


class ApiClick:
    def api_click(self, url):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "thumbuporcancel",
            "paperid": 5
        }
        session = GetSession().get_session()
        return session.post(url, json=data, headers=headers)
