from time import sleep

import pytest

import api
from api.api_add_account import ApiAddAccount
from api.api_delete_account import ApiDeleteAccount
from api.api_list_account import ApiListAccount
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession
from tool.read_yaml import read_yaml


class TestAddAccount:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    @pytest.mark.parametrize('url, realname, username, password, number, desc, type,expect_code,expect_msg',
                             read_yaml('add_account.yaml'))
    def test_add_account(self,url, realname, username, password, number, desc, type,expect_code,expect_msg):
        self.add = ApiAddAccount().api_add_account_post(url, realname, username, password, number, desc, type)
        assert self.add.status_code == expect_code
        assert self.add.json()['ret'] == expect_msg
        re = ApiListAccount().api_list_get(
            url = url,
            page_size=10,
            page_num=1,
            keywords=realname
        )
        assert re.json()['total'] == 1
        ApiDeleteAccount().api_delete_account(url=url,id=self.add.json()['id'])