import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sleep(n_secs):
    time.sleep(n_secs)


def setup_hook():
    print("前置操作：setup!")


def teardown_hook():
    print("后置操作：teardown!")


def get_date():
    struct_time = time.localtime()
    return '-'.join([str(struct_time.tm_year), str(struct_time.tm_mon), str(struct_time.tm_mday)])



