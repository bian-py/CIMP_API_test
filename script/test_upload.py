import api
from api.api_login import ApiLogin
from api.api_logout import ApiLogout
from api.api_upload_picture import ApiUpload
from tool.get_session import GetSession


class TestUpload:
    @classmethod
    def setup_class(cls):
        ApiLogin().api_login_post(url=api.login_url, username='byhy', password='111111')

    @classmethod
    def teardown_class(cls):
        ApiLogout().Api_logout_post(url=api.logout_url)
        GetSession().clear_session()

    def test_upload(self):
        self.upload = ApiUpload().api_upload(api.picture_url)
        assert self.upload.status_code == 200
        assert self.upload.json()['ret'] == 0
