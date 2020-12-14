import pytest

import api
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession
from tool.read_yaml import read_yaml


class TestLogin:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    @pytest.mark.parametrize('url, username, password, expect_code, expect_msg, expect_full', read_yaml('login.yaml'))
    def test_login(self, url, username, password, expect_code, expect_msg, expect_full):
        self.login = ApiLogin().api_login_post(url, username, password)
        try:
            assert self.login.status_code == expect_code
        except:
            raise
        try:
            assert self.login.json()['ret'] == expect_msg
        except:
            raise
        try:
            assert self.login.json() == expect_full
        except:
            raise
