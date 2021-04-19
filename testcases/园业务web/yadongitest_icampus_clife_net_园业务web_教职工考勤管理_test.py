# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\园业务web\yadongitest.icampus.clife.net_园业务web_教职工考勤管理.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.园业务web.yadongitest_icampus_clife_net_园业务web_登陆_test import (
    TestCaseYadongitestIcampusClifeNet园业务Web登陆 as YadongitestIcampusClifeNet园业务Web登陆,
)


class TestCaseYadongitestIcampusClifeNet园业务Web教职工考勤管理(HttpRunner):

    config = (
        Config("教职工考勤管理模块")
        .variables(
            **{
                "Protocol": "${ENV(Protocol)}",
                "host": "${ENV(HOST)}",
                "domainName": "${ENV(DONAIN_NAME)}",
            }
        )
        .verify(False)
    )

    teststeps = [
        Step(
            RunTestCase("园业务_登陆")
            .call(YadongitestIcampusClifeNet园业务Web登陆)
            .export(*["token"])
        ),
        Step(
            RunRequest("考勤班次")
            .get("$Protocol://$host/v1/web/edugarden/attendance/shift/list")
            .with_params(**{"pageIndex": "1", "pageRows": "20"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("考勤班次详情")
            .post("$Protocol://$host/v1/web/edugarden/attendance/shift/get")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "22",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Host": "$host",
                    "Origin": "$Protocol://$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .with_data({"shiftId": "18797967310849"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("考勤班次编辑")
            .post("$Protocol://$host/v1/web/edugarden/attendance/shift/insertOrUpdate")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "377",
                    "Content-Type": "application/json",
                    "Host": "$host",
                    "Origin": "$Protocol://$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .with_json(
                {
                    "clockOneCurrentMorrow": 1,
                    "clockOneNeed": 1,
                    "clockTimeOne": "08:00:00",
                    "clockTimeOneBegin": "06:00:00",
                    "clockTimeOneEnd": "10:00:00",
                    "clockType": 1,
                    "closingOneCurrentMorrow": 1,
                    "closingOneNeed": 1,
                    "closingTimeOne": "18:00:00",
                    "closingTimeOneBegin": "16:00:00",
                    "closingTimeOneEnd": "20:00:00",
                    "shiftId": "18797967310849",
                    "shiftName": "默认班次",
                    "unit1": 1,
                    "unit2": 1,
                    "unit3": 1,
                    "unit4": 1,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.data", "成功")
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/shift/selectAll")
            .post("$Protocol://$host/v1/web/edugarden/attendance/shift/selectAll")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Host": "$host",
                    "Origin": "$Protocol://$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .with_data({})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/holiday/selectAll")
            .get("$Protocol://$host/v1/web/edugarden/holiday/selectAll?")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/group/list")
            .get("$Protocol://$host/v1/web/edugarden/attendance/group/list")
            .with_params(**{"pageIndex": "1", "pageRows": "20"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/shift/getInUseShift")
            .get("$Protocol://$host/v1/web/edugarden/attendance/shift/getInUseShift")
            .with_params(
                **{"endTime": "${get_date()}", "startTime": "${get_date(-12)}"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/statistics/monthDataList")
            .get(
                "$Protocol://$host/v1/web/edugarden/attendance/statistics/monthDataList"
            )
            .with_params(
                **{
                    "endTime": "${get_date()}",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "startTime": "${get_date(-12)}",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/statistics/originalRecordList")
            .get(
                "$Protocol://$host/v1/web/edugarden/attendance/statistics/originalRecordList"
            )
            .with_params(
                **{
                    "endTime": "${get_date()}",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "startTime": "${get_date(-12)}",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/school/%E5%9B%BE%E7%89%87")
            .get("$Protocol://$host/school/%E5%9B%BE%E7%89%87")
            .with_headers(
                **{
                    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Host": "$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                }
            )
            .validate()
            .assert_equal("status_code", 500)
            .assert_equal('headers."Content-Type"', "text/html")
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/group/selectAll")
            .get("$Protocol://$host/v1/web/edugarden/attendance/group/selectAll?")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/attendance/group/getAttGroupStaffList")
            .get(
                "$Protocol://$host/v1/web/edugarden/attendance/group/getAttGroupStaffList"
            )
            .with_params(
                **{"groupId": "19095106486273", "pageIndex": "1", "pageRows": "20"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLhttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseYadongitestIcampusClifeNet园业务Web教职工考勤管理().test_start()
