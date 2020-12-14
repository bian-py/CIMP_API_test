from tool.get_session import GetSession


class ApiFbSet:
    def api_fb_set(self, url):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "set",
                "name": "homepage",
                "value": "{\"news\":[5],\"notice\":[1],\"paper\":[5]}"}
        session = GetSession().get_session()
        return session.post(url, json=data,headers=headers)
