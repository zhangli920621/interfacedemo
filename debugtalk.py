import time
import datetime
from httprunner import __version__


def get_httprunner_version():
    return __version__


def setup_hook():
    print("前置操作：setup!")


def teardown_hook():
    print("后置操作：teardown!")


def get_date(days=0):
    if days == 0:
        date = (datetime.datetime.now()).strftime("%Y-%m-%d")
    else:
        date = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    return str(date)

