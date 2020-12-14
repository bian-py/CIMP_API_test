from tool.get_session import GetSession


class ApiNoticeOne:
    def api_notice_one(self, url, id):
        session = GetSession().get_session()
        params = {'action': 'getone',
                  'id': id
                  }
        return session.get(url, params=params)
