import api
from api.api_add_account import ApiAddAccount
from api.api_delete_account import ApiDeleteAccount
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession


class TestDeleteAccount:
    id = None

    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')
        re = ApiAddAccount().api_add_account_post(url='http://127.0.0.1//api/account',
                                                  realname='王小明',
                                                  username='wangxiaoming',
                                                  password='123456',
                                                  number='123465',
                                                  desc='新增用户',
                                                  type=2000)
        cls.id = re.json()['id']

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession.clear_session()

    def test_delete_account(self):
        self.delete = ApiDeleteAccount().api_delete_account(api.account_url,self.id)
        assert self.delete.status_code == 200
        assert self.delete.json()['ret'] == 0
