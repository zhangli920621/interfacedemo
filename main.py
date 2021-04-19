#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author :   alisa_l_zhang
# @Time：     2021/4/7 15:50
# @File Name：   main.py
# @Description : PyCharm
import logging
import os
from util.functions import send_mail

if __name__ == "__main__":
    logging.basicConfig()
    cmd1 = 'cd ..'
    cmd2 = 'hrun interfacedemo --alluredir=./interfacedemo/tmp/allure_results --clean-alluredir'
    cmd3 = 'allure generate ./interfacedemo/tmp/allure_results -o ./interfacedemo/tmp/allure-report --clean'
    try:
        os.system('{} && {}'.format(cmd1, cmd2))
    except Exception as e:
        logging.INFO(e)
    finally:
        # 生成Allure报告
        os.system('{} && {}'.format(cmd1, cmd3))
        send_mail()
