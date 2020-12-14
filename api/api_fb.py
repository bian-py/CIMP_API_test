from tool.get_session import GetSession


class ApiFb:
    def api_fb_get(self, url):
        params = {"action": "gethomepagebyconfig"}
        session = GetSession().get_session()
        return session.get(url, params=params)
