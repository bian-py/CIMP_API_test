import pytest

import api
from tool.get_session import GetSession
from tool.run_sql import run_sql


class TestWorkFlow:
    wk_id = None

    @classmethod
    def setup_class(cls):
        run_sql('delete from cimp_wf_design where creator_id = 12 ')
        run_sql('delete from cimp_wf_design_step where operator_id = 12 or operator_id = 13')
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "signin",
            "username": 'test01',
            "password": '123456'
        }
        data2 = {
            "action": "signin",
            "username": 'Test01',
            "password": '123456'
        }
        GetSession.get_session().post(api.login_url, json=data, headers=headers)
        GetSession.get_session2().post(api.login_url, json=data2, headers=headers)

    @classmethod
    def teardown_class(cls):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "signout"
        }
        GetSession.get_session().post(api.logout_url, json=data, headers=headers)
        GetSession.get_session2().post(api.login_url, json=data, headers=headers)
        GetSession().clear_session()
        GetSession().clear_session2()

    @classmethod
    def modify_id(cls, wk_id):
        cls.wk_id = wk_id

    @pytest.mark.run(order=1)
    def test01_create(self):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "stepaction",
                "key": "create_topic",
                "wf_id": -1,
                "submitdata": [{"name": "毕业设计标题", "type": "text", "value": "test01的毕业设计2"},
                               {"name": "主题描述", "type": "richtext", "value": "这是我的毕业设计11111113"}]}
        re1 = GetSession.get_session().post(url=api.work_flow, json=data, headers=headers)
        assert re1.json()['ret'] == 0
        self.modify_id(re1.json()['wf_id'])

    @pytest.mark.run(order=2)
    def test02_reject(self):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "stepaction",
                "key": "reject_topic",
                "wf_id": self.wk_id,
                "submitdata": [{"name": "驳回原因", "type": "textarea", "value": "asdfsadfasfasfdf"}]}
        re2 = GetSession.get_session2().post(url=api.work_flow, json=data, headers=headers)
        assert re2.json()['ret'] == 0
        # cls.wk_id = re2.json()['wf_id']

    @pytest.mark.run(order=3)
    def test03_modify(self):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "stepaction",
                "key": "modify_topic",
                "wf_id": self.wk_id,
                "submitdata": [{"name": "毕业设计标题", "type": "text", "value": "test01的毕业设计2"},
                               {"name": "主题描述", "type": "richtext", "value": "这是我的毕业设计11111113"}]}
        re1 = GetSession.get_session().post(url=api.work_flow, json=data, headers=headers)
        assert re1.json()['ret'] == 0
        # cls.wk_id = re1.json()['wf_id']

    @pytest.mark.run(order=4)
    def test04_approve(self):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "stepaction",
                "key": "approve_topic",
                "wf_id": self.wk_id,
                "submitdata": [{"name": "备注", "type": "richtext", "value": "222222222222222222222222222222"}]}
        re2 = GetSession.get_session2().post(url=api.work_flow, json=data, headers=headers)
        assert re2.json()['ret'] == 0

    @pytest.mark.run(order=5)
    def test05_submit(self):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "stepaction",
                "key": "submit_design",
                "wf_id": self.wk_id,
                "submitdata": [{"name": "毕业设计内容", "type": "richtext", "value": "898494949849494984949444498498449"}]}
        re1 = GetSession.get_session().post(url=api.work_flow, json=data, headers=headers)
        assert re1.json()['ret'] == 0

    @pytest.mark.run(order=6)
    def test06_score(self):
        headers = {'Content-Type': 'application/json'}
        data = {"action": "stepaction",
                "key": "score_design",
                "wf_id": self.wk_id,
                "submitdata": [{"name": "得分", "type": "int", "value": 100},
                               {"name": "备注", "type": "richtext", "value": "8949498191919191981981"}]}
        re2 = GetSession.get_session2().post(url=api.work_flow, json=data, headers=headers)
        assert re2.json()['ret'] == 0

    @pytest.mark.run(order=7)
    def test07_list_all(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            "action": "signin",
            "username": 'byhy',
            "password": '111111'
        }
        GetSession.get_session().post(api.login_url, json=data, headers=headers)
        params = {'action': 'listbypage',
                  'pagesize': 10,
                  'pagenum': 1,
                  'keywords': ''}
        re = GetSession.get_session().get(api.work_flow, params=params)
        assert re.status_code == 200
        assert re.json()['ret'] == 0
        assert re.json()['total'] == 4

    @pytest.mark.run(order=8)
    def test08_get_one(self):
        headers = {'Content-Type': 'application/json'}
        params = {'action': 'getone',
                  'wf_id': self.wk_id,
                  'keywords': ''}
        re = GetSession.get_session().get(api.work_flow, params=params)
        assert re.status_code == 200
        assert re.json()['ret'] == 0

    @pytest.mark.run(order=9)
    def test09_check_step(self):
        result = ('{"ret": 0, "data": [{"name": "毕业设计标题", "type": "text", "value": '
                  '"阿水电费水电费水电费ds"}, {"name": "主题描述", "type": "textarea", "value": '
                  '"阿萨德但是但是是的是第三方第三方是否但是"}]}')

        params = {'action': 'getstepactiondata',
                  'step_id': 12}
        re = GetSession.get_session().get(api.work_flow, params=params)
        assert re.status_code == 200
        assert re.text == result
