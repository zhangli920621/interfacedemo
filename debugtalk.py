from httprunner import __version__
import datetime
import pymysql
import subprocess


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


# 数据库获取数据
def sql_res(cmd):
    conn = pymysql.connect(host="10.6.14.11", port=29966, user="root", password="123456",
                           database="db_campus_education", charset="utf8")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(cmd)
    res = cursor.fetchall()
    cursor.close()
    cursor.close()
    return res

