from tool.get_session import GetSession


class ApiNoticeAll:
    def api_notice_all(self, url, page_size, page_num, keywords=None):
        session = GetSession().get_session()
        params = {'action': 'listbypage_allstate',
                  'pagesize': page_size,
                  'pagenum': page_num,
                  'keywords': keywords,
                  }
        return session.get(url, params=params)
