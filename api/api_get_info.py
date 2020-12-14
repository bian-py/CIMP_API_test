from tool.get_session import GetSession


class ApiGetInfo:
    def api_info(self, url):
        params = {"action": "getmyprofile"}
        session = GetSession().get_session()
        return session.get(url,params=params)
