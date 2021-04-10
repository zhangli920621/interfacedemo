#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author :   alisa_l_zhang
# @Time：     2021/4/7 19:33
# @File Name：   functions.py
# @Description : PyCharm
import argparse
import hashlib
import time


def toISO(t):
    return t.encode("utf8").decode("iso8859-1")


