import unittest
import requests

class TestComment(unittest.TestCase):
    def test_case1(self):
        """
        评论中文
        :return:
        """
        header = {"Content-Type": "application/json"}
        data = '{"news_id":"14","comment":"中文"}'.encode('utf-8')
        cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
        r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
        assert r.json()['data']['content'] == "中文" and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"
    def test_case2(self):
        """
        评论英文
        :return:
        """
        header = {"Content-Type": "application/json"}
        data = '{"news_id":"14","comment":"hello"}'.encode('utf-8')
        cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
        r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
        assert r.json()['data']['content'] == "hello" and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"
    def test_case3(self):
        """
        评论特殊字符
        :return:
        """
        header = {"Content-Type": "application/json"}
        data = '{"news_id":"14","comment":"##&&**"}'.encode('utf-8')
        cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
        r = requests.post("http://info.itfeat.com/news/news_comment", data=data, headers=header, cookies=cookie)
        assert r.json()['data']['content'] == "##&&**" and r.json()['errmsg'] == "OK" and r.json()['errno'] == "0"