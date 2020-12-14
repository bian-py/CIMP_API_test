from tool.get_session import GetSession


class ApiAddNotice:
    def api_add_notice_post(self, url, title,content):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "addone",
            "data": {
                "title": title,
                "content": content
            }
        }
        session = GetSession().get_session()
        return session.post(url, json=data, headers=headers)
