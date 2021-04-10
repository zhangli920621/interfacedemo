import configparser
import os
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


def get_env_value(data, _type='str'):
    dic = {}
    env_file = '{}/.env'.format(os.path.dirname(__file__))
    with open(env_file) as env_file:
        for line in env_file:
            if not len(line) or line.startswith('#'):
                continue
            key, value = line.replace('\n', '').partition('=')[::2]
            dic[key] = value

    if _type == 'list':
        return [dic[data]]
    else:
        return dic[data]


# print(get_env_value('GARDEN_USERNAME'))
# print(get_env_value('GARDEN_USERNAME', 'list'))