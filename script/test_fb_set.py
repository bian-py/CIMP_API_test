import api
from api.api_fb_set import ApiFbSet
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from tool.get_session import GetSession


class TestFbSet:

    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        GetSession().get_session().post(api.fb_url,
                                        json={"action": "set",
                                              "name": "homepage",
                                              "value": "{\"news\":[5,7,6,3,4],\"notice\":[1,3,5,2]"
                                                       ",\"paper\":[5,9,10,4,8]}"},
                                        headers={'Content-Type': 'application/json'})
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession().clear_session()

    def test_fb_set(self):
        self.set = ApiFbSet().api_fb_set(api.fb_url)
        assert self.set.status_code == 200
        assert self.set.json()['ret'] == 0

