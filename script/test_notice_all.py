import pytest

import api
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from api.api_notice_all import ApiNoticeAll
from tool.get_session import GetSession
from tool.read_yaml import read_yaml


class TestNoticeAll:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    @pytest.mark.parametrize('url, page_size, page_num, keywords,expect_code,expect_msg',
                             read_yaml('notice_all.yaml'))
    def test_notice_all(self, url, page_size, page_num, keywords, expect_code, expect_msg):
        self.notice = ApiNoticeAll().api_notice_all(url, page_size, page_num, keywords)
        assert self.notice.status_code == expect_code
        assert [self.notice.json()['ret'], self.notice.json()['total']] == expect_msg
