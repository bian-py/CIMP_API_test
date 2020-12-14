import api
from api.api_banone_notice import ApiBanNotice
from api.api_delete_notice import ApiDeletenotice
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from api.api_notic_add import ApiAddNotice
from api.api_publishone_notice import ApiPublishNotice
from tool.get_session import GetSession


class TestDeleteNotice:
    id = None

    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')
        re = ApiAddNotice().api_add_notice_post(url=api.notice_url, title='这是测试通知的标题', content='这是测试通知的内容')
        cls.id = re.json()['id']
        ApiBanNotice().api_ban_notice(api.notice_url, cls.id)

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    def test_publish_notice(self):
        self.publish = ApiPublishNotice().api_publish_notice(api.notice_url,self.id)
        assert self.publish.status_code == 200
        assert self.publish.json()['ret'] == 0
        assert self.publish.json()['status'] == 1
        ApiDeletenotice().api_delete_account(api.notice_url, self.id)
