from tokenize import cookie_re

import requests

# 添加path参数
# r = requests.get("http://info.itfeat.com/news/14")
# print(r.text)
# 添加query参数
# r = requests.get("http://info.itfeat.com/news_list?cid=3&page=2")
# print(r.text)
# data = {"cid":"3","page":"2"}
# r = requests.get("http://info.itfeat.com/news_list" , params=data)
# print(r.text)
# 添加form文本
# data = {"mobile":"15666820414","password":"123456"}
# r = requests.post("http://info.itfeat.com/passport/login" , data=data)
# print(r.json())

# 添加请求头 请求体 cookie
# header = {"Content-Type":"application/json"}
# data = '{"news_id":"14","comment":"你好"}'.encode("utf-8")
# cookie = {"session":"3971f8b6-a354-4813-a879-62ea0ed9fac3.Fv8VxxQSs9oi5LU4GOKuTOaib48"}
# r = requests.post("http://info.itfeat.com/news/news_comment", headers=header, data=data,cookies=cookie)
# print(r.json())

# 添加form文件
cookie = {"session":"3971f8b6-a354-4813-a879-62ea0ed9fac3.Fv8VxxQSs9oi5LU4GOKuTOaib48"}
with open("./b.jpg", "rb") as f:
    file = {"avatar":f}
    r = requests.post("http://info.itfeat.com/user/pic_info", cookies=cookie, files=file)
print(r.text)