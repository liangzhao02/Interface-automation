import unittest
from ddt import ddt,data,unpack

@ddt
class TestParmas(unittest.TestCase):

    @data("中文","hello","##**")
    def test_case1(self, text):
        """
        评论
        :return:
        """
        print("我的评论内容是%s" % text)

    @data(["zs","zs123"],["ls","ls123"])
    @unpack
    def test_case2(self, username, password):
        """
        登录
        zs zs123
        ls ls123
        :return:
        """
        print("我的账号是%s,我的密码是%s" % (username, password))
