import requests


class GetSession:
    __session = None
    __session2 = None

    @classmethod
    def get_session(cls):
        if cls.__session is None:
            cls.__session = requests.Session()
            return cls.__session
        else:
            return cls.__session
        # return requests.Session()

    @classmethod
    def get_session2(cls):
        if cls.__session2 is None:
            cls.__session2 = requests.Session()
            return cls.__session2
        else:
            return cls.__session2
        # return requests.Session()

    @classmethod
    def clear_session(cls):
        cls.__session = None

    @classmethod
    def clear_session2(cls):
        cls.__session2 = None




