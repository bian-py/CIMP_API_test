from time import sleep

from appium import webdriver

from config import cap, cap2, cap3
from tool.get_log import GetLogger

log = GetLogger.get_log()


class GetDriver:
    __driver1 = None
    __driver2 = None
    __driver3 = None

    @classmethod
    def get_app_driver(cls):
        log.info(f"正在获取app驱动对象，启动参数是{cap2}")
        if cls.__driver1 is None:
            cls.__driver1 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap2)
            return cls.__driver1
        else:
            return cls.__driver1

    @classmethod
    def quit_app_driver(cls):
        log.info('关闭驱动对象，并置空')
        cls.__driver1.terminate_app('net.mirrormx.livechat')
        cls.__driver1.quit()
        cls.__driver1 = None

    @classmethod
    def get_app_driver2(cls):
        log.info(f"正在获取app驱动对象，启动参数是{cap3}")
        if cls.__driver2 is None:
            cls.__driver2 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap3)
            return cls.__driver2
        else:
            return cls.__driver2

    @classmethod
    def quit_app_driver2(cls):
        log.info('关闭驱动对象，并置空')
        cls.__driver2.terminate_app('net.mirrormx.livechat')
        cls.__driver2.quit()
        cls.__driver2 = None

    @classmethod
    def get_app_driver3(cls):
        log.info(f"正在获取app驱动对象，启动参数是{cap}")
        if cls.__driver3 is None:
            cls.__driver3 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            return cls.__driver3
        else:
            return cls.__driver3

    @classmethod
    def quit_app_driver3(cls):
        log.info('关闭驱动对象，并置空')
        cls.__driver3.terminate_app('net.mirrormx.livechat')
        cls.__driver3.quit()
        cls.__driver3 = None
