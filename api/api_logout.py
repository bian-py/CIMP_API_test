from tool.get_session import GetSession


class ApiLogout:

    def Api_logout_post(self, url):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "signout"
        }
        session = GetSession.get_session()
        return session.post(url, json=data, headers=headers)
