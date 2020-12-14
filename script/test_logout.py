import pytest

import api
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession
from tool.read_yaml import read_yaml


class TestLogout:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        GetSession.clear_session()

    @pytest.mark.parametrize('url, username, password,expect_code,expect_msg,expect_headers',
                             read_yaml('logout_prepare.yaml'))
    def test_logout(self, url, username, password, expect_code, expect_msg, expect_headers):
        ApiLogin().api_login_post(url, username, password)
        self.logout = ApiLogout().Api_logout_post(url=api.logout_url)
        assert self.logout.status_code == expect_code
        assert self.logout.json() == expect_msg
        assert expect_headers in self.logout.headers['Set-Cookie']


