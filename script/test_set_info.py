import api
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from api.api_post_info import ApiSetInfo
from tool.get_session import GetSession


class TestSetInfo:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='test01', password='123456')

    @classmethod
    def teardown_class(cls):
        ApiSetInfo().api_set_info(name='学员1', url=api.info_url)
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession().clear_session()

    def test_info(self):
        self.info = ApiSetInfo().api_set_info(name='修改', url=api.info_url)
        assert self.info.status_code == 200
        assert self.info.json()['ret'] == 0
