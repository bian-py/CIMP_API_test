import api
from api.api_fb import ApiFb
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession


class TestFb:

    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession().clear_session()

    def test_fb_get(self):
        self.fb = ApiFb().api_fb_get(api.fb_url)
        assert self.fb.status_code == 200
        assert self.fb.json()['ret'] == 0
