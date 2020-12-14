from tool.get_session import GetSession


class ApiListAccount:

    def api_list_get(self, url, page_size, page_num, keywords=None):
        session = GetSession().get_session()
        params = {'action': 'listbypage',
                  'pagesize': page_size,
                  'pagenum': page_num,
                  'keywords': keywords}
        return session.get(url, params=params)
