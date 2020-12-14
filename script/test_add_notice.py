import api
from api.api_delete_notice import ApiDeletenotice
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from api.api_notic_add import ApiAddNotice
from tool.get_session import GetSession


class TestNoticeAdd:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    def test_add_notice(self, url=api.notice_url, title='这是测试通知的标题', content='这是测试通知的内容'):
        self.add = ApiAddNotice().api_add_notice_post(url, title, content)
        assert self.add.status_code == 200
        assert self.add.json()['ret'] == 0
        ApiDeletenotice().api_delete_account(api.notice_url, self.add.json()['id'])
