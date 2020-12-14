import api
from api.api_get_info import ApiGetInfo
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession


class TestInfo:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='test01', password='123456')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession().clear_session()

    def test_info(self):
        self.info = ApiGetInfo().api_info(api.info_url)
        assert self.info.status_code == 200
        assert self.info.json()['ret'] == 0
