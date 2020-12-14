import pytest

import api
from api.api_list_account import ApiListAccount
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession
from tool.read_yaml import read_yaml


class TestListAccount:

    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    @pytest.mark.parametrize('url,page_size,page_num,keywords,expect_code,expect_msg', read_yaml('list_account.yaml'))
    def test_list_account(self, url, page_size, page_num, keywords, expect_code, expect_msg):
        self.list = ApiListAccount().api_list_get(url, page_size, page_num, keywords)
        assert self.list.status_code == expect_code
        assert self.list.json() == expect_msg
