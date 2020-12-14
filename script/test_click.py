import api
from api.api_click import ApiClick
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession


class TestClick:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='test01', password='123456')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession().clear_session()

    def test_click(self):

        self.click = ApiClick().api_click(api.info_url)
        assert self.click.status_code == 200
        assert self.click.json() == {'ret': 0, 'thumbupcount': 2}
        self.click2 = ApiClick().api_click(api.info_url)
        assert self.click2.status_code == 200
        assert self.click2.json() == {'ret': 0, 'thumbupcount': 1}