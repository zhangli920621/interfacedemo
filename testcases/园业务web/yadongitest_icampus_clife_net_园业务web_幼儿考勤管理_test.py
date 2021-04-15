# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\园业务web\yadongitest.icampus.clife.net_园业务web_幼儿考勤管理.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.园业务web.yadongitest_icampus_clife_net_园业务web_登陆_test import (
    TestCaseYadongitestIcampusClifeNet园业务Web登陆 as YadongitestIcampusClifeNet园业务Web登陆,
)


class TestCaseYadongitestIcampusClifeNet园业务Web幼儿考勤管理(HttpRunner):

    config = (
        Config("幼儿考勤管理模块")
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
            RunRequest("全园概况")
            .get("$Protocol://$host/v1/web/edugarden/statistic/attendanceStatistic")
            .with_params(**{"date": "${get_date()}"})
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("获取{年级{班级}} 二级树形结构")
            .get("$Protocol://$host/v1/web/edugarden/statistic/selectClass?")
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("班级概况")
            .get("$Protocol://$host/v1/web/edugarden/statistic/classOverview")
            .with_params(
                **{"classId": "11666912313345", "date": "${get_date()}", "gradeId": "5"}
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v1/web/edugarden/statistic/classStatistic")
            .get("$Protocol://$host/v1/web/edugarden/statistic/classStatistic")
            .with_params(
                **{
                    "date": "${get_date()}",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "sort": "0",
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("每日统计列表数据")
            .get("$Protocol://$host/v1/web/edugarden/attendance/student/getDailyList")
            .with_params(
                **{"pageIndex": "1", "pageRows": "20", "statisticDate": "${get_date()}"}
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("月度数据-获取月度数据列表")
            .get(
                "$Protocol://$host/v1/web/edugarden/attendance/student/getStuAttReportPager"
            )
            .with_params(
                **{
                    "endDate": "${get_date()}",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "startDate": "${get_date(-12)}",
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("原始记录")
            .get("$Protocol://$host/v1/web/edugarden/original/list")
            .with_params(
                **{
                    "endDate": "${get_date()}",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "startDate": "${get_date(-12)}",
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("出勤设置-展示已有的设置")
            .get("$Protocol://$host/v1/web/edugarden/infantAttendance/list?")
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
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("出勤设置-保存")
            .post("$Protocol://$host/v1/web/edugarden/infantAttendance/setting")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Length": "1742",
                    "Content-Type": "application/json",
                    "Host": "$host",
                    "Origin": "$Protocol://$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$domainName",
                }
            )
            .with_json(
                {
                    "broadcastList": [
                        {"message": "欢迎{sn}小朋友入园", "type": 1},
                        {"message": "{sn}小朋友，家长来接啦", "type": 2},
                    ],
                    "endTime": "23:00:00",
                    "holidayWeek": "1-2-3-4-5-6",
                    "noList": [
                        {
                            "className": None,
                            "createTime": "2021-04-12 15:04:33",
                            "deleted": 1,
                            "orgId": 6438733348866,
                            "remark": "234567890-=-09呕iu预热我去而退哦iu犹太人被1234",
                            "sex": None,
                            "status": None,
                            "studentId": 23841850654721,
                            "studentName": None,
                            "updateTime": "2021-04-12 15:04:33",
                        }
                    ],
                    "permit": 1,
                    "ruleList": [
                        {
                            "amNormalTime": "09:20:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 5,
                            "gradeName": "托班",
                            "orgId": 6438733348866,
                            "pmNormalTime": "11:00:00",
                            "ruleId": 16815940567041,
                            "updateTime": "2021-04-12 15:04:33",
                            "uuid": "c8450bc7-d5d2-4bab-8754-0b77d355a5aa",
                        },
                        {
                            "amNormalTime": "10:10:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 6,
                            "gradeName": "小班",
                            "orgId": 6438733348866,
                            "pmNormalTime": "13:30:00",
                            "ruleId": 16815940567042,
                            "updateTime": "2021-04-12 15:04:33",
                            "uuid": "7aaef610-a827-42be-8af7-f2ece4b46b30",
                        },
                        {
                            "amNormalTime": "10:00:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 7,
                            "gradeName": "中班",
                            "orgId": 6438733348866,
                            "pmNormalTime": "14:30:00",
                            "ruleId": 16815940567043,
                            "updateTime": "2021-04-12 15:04:33",
                            "uuid": "f7e643dd-d19a-4c30-80e2-9f806f4a5c7b",
                        },
                        {
                            "amNormalTime": "12:00:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 8,
                            "gradeName": "大班",
                            "orgId": 6438733348866,
                            "pmNormalTime": "15:11:00",
                            "ruleId": 16815940567044,
                            "updateTime": "2021-04-12 15:04:33",
                            "uuid": "cb6b998b-c3f3-45d9-8f06-4f8ea4509655",
                        },
                        {
                            "amNormalTime": "12:50:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 9,
                            "gradeName": "学前班",
                            "orgId": 6438733348866,
                            "pmNormalTime": "18:00:00",
                            "ruleId": 16815940567045,
                            "updateTime": "2021-04-12 15:04:33",
                            "uuid": "07d1e632-fe67-44b0-a59f-a3e1bab0c3f6",
                        },
                    ],
                    "startTime": "07:00:00",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
            .assert_equal("body.data", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCaseYadongitestIcampusClifeNet园业务Web幼儿考勤管理().test_start()
