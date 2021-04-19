#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author :   alisa_l_zhang
# @Time：     2021/4/7 19:33
# @File Name：   functions.py
# @Description : PyCharm
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def toISO(t):
    return t.encode("utf8").decode("iso8859-1")


def send_mail():
    # 测试报告发邮件通知
    from_addr = '826369072@qq.com'  # 邮件发送账号
    to_addrs = 'alisa_l_zhang@163.com'  # 接收邮件账号
    qqCode = 'wipfwhdhnkdabfia'  # 授权码
    # 组装发送内容
    msg = '''
        <p>Python接口自动化结果发送... </p>
        <br/>
        <p><a href="http://localhost:63342/DiangoDemo/tmp/allure-report/index.html">点击查看测试报告</a></p>
    '''
    message = MIMEText(msg, 'html', _charset="utf-8")  # 发送的内容
    subject = 'Httprunner 接口自动化测试'
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题
    message['From'] = Header("Python邮件预警系统", 'utf-8')
    message['To'] = Header("管理员", 'utf-8')
    # 配置服务器
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, qqCode)
    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
        print('邮件发送成功~~')
    except Exception as e:
        print('邮件发送失败--' + str(e))


