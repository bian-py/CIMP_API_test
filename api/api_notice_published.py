from tool.get_session import GetSession


class ApiNoticePublished:
    def api_notice_published_get(self, url, page_size, page_num, keywords=None):
        session = GetSession().get_session()
        params = {'action': 'listbypage',
                  'pagesize': page_size,
                  'pagenum': page_num,
                  'keywords': keywords,
                  'withoutcontent': 'true'}
        return session.get(url, params=params)
