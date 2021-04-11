# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\园业务web\yadong.campus.clife.cn_园业务web_幼儿考勤管理.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseYadongCampusClifeCn园业务Web幼儿考勤管理(HttpRunner):

    config = (
        Config("园业务web_幼儿考勤管理")
        .variables(
            **{
                "Protocol": "${ENV(Protocol)}",
                "host": "${ENV(HOST)}",
                "donainname": "${ENV(DONAIN_NAME)}",
            }
        )
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("园业务web_登陆")
            .post("$Protocol://$host/v1/web/eduaccount/sys/login")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Connection": "keep-alive",
                    "Content-Length": "76",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Host": "$host",
                    "Origin": "$Protocol://$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
                }
            )
            .with_data(
                {
                    "systemCode": "garden",
                    "username": "${ENV(GARDEN_USERNAME)}",
                    "password": "${ENV(GARDEN_PASSWORD)}",
                }
            )
            .extract()
            .with_jmespath("body.data.token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("数据字典-所有字典")
            .get("$Protocol://$host/v1/web/edumanage/system/allDict?")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("省市区级联-根据国家标识获取省份、城市、地区数据")
            .get("$Protocol://$host/v1/web/edumanage/provincialCascade/all?")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("登录相关-获取身份列表")
            .get("$Protocol://$host/v1/web/eduaccount/user/identitys")
            .with_params(
                **{"pageIndex": "1", "pageRows": "12", "systemCode": "district"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("登录相关-根据域名获取机构简介")
            .get("$Protocol://$host/v1/web/eduaccount/org/getOrgByDomainName")
            .with_params(**{"domainName": "$donainname"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("应用-列表收藏应用（账号收藏的应用）")
            .get("$Protocol://$host/v1/web/edudistrict/apps/personal")
            .with_params(**{"platform": "1"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("全园概况")
            .get("$Protocol://$host/v1/web/edugarden/statistic/attendanceStatistic")
            .with_params(**{"date": "2021-04-08"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                **{"classId": "16807134625793", "date": "2021-04-08", "gradeId": "5"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                    "date": "2021-04-08",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "sort": "0",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                **{
                    "pageIndex": "1",
                    "pageRows": "20",
                    "results": "1",
                    "statisticDate": "2021-04-08",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                    "endDate": "2021-04-08",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "startDate": "2021-04-01",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                    "endDate": "2021-04-08",
                    "pageIndex": "1",
                    "pageRows": "20",
                    "startDate": "2021-04-01",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=utf-8",
                    "Host": "$host",
                    "Pragma": "no-cache",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Connection": "keep-alive",
                    "Content-Length": "1785",
                    "Content-Type": "application/json",
                    "Host": "$host",
                    "Origin": "$Protocol://$host",
                    "Referer": "$Protocol://$host/school/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
                    "X-Access-Token": "$token",
                    "X-Requested-With": "XMLHttpRequest",
                    "domainName": "$donainname",
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
                            "className": "托四班",
                            "createTime": "2021-04-02 16:02:04",
                            "deleted": 1,
                            "orgId": 6672712597506,
                            "remark": "中秋节：2021-09-19~2021-09-21国庆节：2021端午节：2021-06-1端45",
                            "sex": 2,
                            "status": 1,
                            "studentId": 16812585123841,
                            "studentName": "亚东幼儿园宝宝七号",
                            "updateTime": "2021-04-02 16:02:04",
                        }
                    ],
                    "permit": 1,
                    "ruleList": [
                        {
                            "amNormalTime": "09:20:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 5,
                            "gradeName": "托班",
                            "orgId": 6672712597506,
                            "pmNormalTime": "11:00:00",
                            "ruleId": 16815940567041,
                            "updateTime": "2021-04-02 16:02:04",
                            "uuid": "0be4cc14-96c4-43ab-85f3-163d515a5ee9",
                        },
                        {
                            "amNormalTime": "10:10:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 6,
                            "gradeName": "小班",
                            "orgId": 6672712597506,
                            "pmNormalTime": "13:30:00",
                            "ruleId": 16815940567042,
                            "updateTime": "2021-04-02 16:02:04",
                            "uuid": "d73c7cbb-3e0e-4d49-90d7-2b7dc88b02a5",
                        },
                        {
                            "amNormalTime": "10:00:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 7,
                            "gradeName": "中班",
                            "orgId": 6672712597506,
                            "pmNormalTime": "14:30:00",
                            "ruleId": 16815940567043,
                            "updateTime": "2021-04-02 16:02:04",
                            "uuid": "a89d2a2b-2052-4e49-aebb-ab7c94746828",
                        },
                        {
                            "amNormalTime": "12:00:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 8,
                            "gradeName": "大班",
                            "orgId": 6672712597506,
                            "pmNormalTime": "15:11:00",
                            "ruleId": 16815940567044,
                            "updateTime": "2021-04-02 16:02:04",
                            "uuid": "3d826002-a3e3-4f59-b389-f2e97a5338e1",
                        },
                        {
                            "amNormalTime": "12:50:00",
                            "createTime": "2021-03-04 22:32:18",
                            "gradeId": 9,
                            "gradeName": "学前班",
                            "orgId": 6672712597506,
                            "pmNormalTime": "18:00:00",
                            "ruleId": 16815940567045,
                            "updateTime": "2021-04-02 16:02:04",
                            "uuid": "0ffa7f19-d1d4-4aea-8dce-f49d3786e596",
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
    TestCaseYadongCampusClifeCn园业务Web幼儿考勤管理().test_start()
