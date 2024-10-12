import unittest
import requests
from ddt import ddt, data, unpack

@ddt
class TestComment(unittest.TestCase):
    # def test_case1(self):
    #     """
    #     评论中文
    #     :return:
    #     """
    #     header = {"Content-Type": "application/json"}
    #     data = '{"news_id":"14","comment":"中文"}'.encode('utf-8')
    #     cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
    #     r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
    #     assert r.json()['data']['content'] == "中文" and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"
    # def test_case2(self):
    #     """
    #     评论英文
    #     :return:
    #     """
    #     header = {"Content-Type": "application/json"}
    #     data = '{"news_id":"14","comment":"hello"}'.encode('utf-8')
    #     cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
    #     r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
    #     assert r.json()['data']['content'] == "hello" and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"
    # def test_case3(self):
    #     """
    #     评论特殊字符
    #     :return:
    #     """
    #     header = {"Content-Type": "application/json"}
    #     data = '{"news_id":"14","comment":"##&&**"}'.encode('utf-8')
    #     cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
    #     r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
    #     assert r.json()['data']['content'] == "##&&**" and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"

    @data("中文","hello","##")
    def test_case1(self ,text):
        header = {"Content-Type": "application/json"}
        data = ('{"news_id":"14","comment":"%s"}' %text).encode('utf-8')
        cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
        r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
        assert r.json()['data']['content'] == text and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"

    @data(
        ['{"news_id":"1","action":"collect"}',"操作成功","0"],
        ['{"news_id":"10086","action":"collect"}',"未查询到新闻数据","4002"],
        ['{"news_id":null,"action":"collect"}',"参数错误","4103"]
    )
    @unpack
    def test_case2(self ,body, errmsg, errno):
        header = {"Content-Type": "application/json"}
        cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
        data = body
        r = requests.post("http://info.itfeat.com/news/news_collect", headers=header, cookies=cookie, data=data)
        assert r.json()['errmsg'] == errmsg and r.json()['errno'] == errno
