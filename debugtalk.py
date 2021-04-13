import time
import datetime
from httprunner import __version__


def get_httprunner_version():
    return __version__


def setup_hook():
    print("前置操作：setup!")


def teardown_hook():
    print("后置操作：teardown!")



# 获取一些时间请求参数格式如‘2021-04-12’
def get_date(days=None):
    if days is None:
        date = (datetime.datetime.now()).strftime("%Y-%m-%d")
    else:
        date = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    return str(date)
