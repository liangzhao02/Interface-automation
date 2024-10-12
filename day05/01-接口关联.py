import requests

# 评论
header = {"Content-Type": "application/json"}
data = '{"news_id":"14","comment":"我是评论"}'.encode('utf-8')
cookie = {"session": "82e4147a-0058-4838-a92e-973d2f504119.My7vjPPqoaD1NtNnPQ-I81ma4d8"}
r = requests.post("http://info.itfeat.com/news/news_comment" , data=data, headers=header, cookies=cookie)
comment_id = r.json()["data"]["id"]
print(r.json())

# 回复评论
data = ('{"news_id":"14","comment":"我是回复评论","parent_id":"%s"}' %comment_id).encode('utf-8')
r = requests.post("http://info.itfeat.com/news/news_comment" , data=data, headers=header, cookies=cookie)
print(r.json())