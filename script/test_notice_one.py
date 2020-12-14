import pytest

import api
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from api.api_notice_getone import ApiNoticeOne
from tool.get_session import GetSession
from tool.read_yaml import read_yaml


class TestNoticeOne:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='test01', password='123456')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    @pytest.mark.parametrize('url,id,expect_code,expect_msg',
                             read_yaml('notice_one.yaml'))
    def test_notice_published(self, url, id, expect_code, expect_msg):
        self.notice = ApiNoticeOne().api_notice_one(url, id)
        assert self.notice.status_code == expect_code
        assert self.notice.json()['ret'] == expect_msg
