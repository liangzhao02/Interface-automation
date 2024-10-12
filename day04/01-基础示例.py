import requests

# r = requests.get('https://www.baidu.com')
# r.encoding = 'utf-8'
# # 查看响应体
# print(r.text)
# # 查看编码格式
# print(r.encoding)
# # 查看响应头
# print(r.headers['Connection'])
# # 查看状态码
# print(r.status_code)
# r = requests.get("http://info.itfeat.com/news_list?cid=3&page=2")
# # 读取json数据 可以将响应的json转为python
# print(r.json()['data']['current_page'])
# 超时
# r = requests.get('https://www.baidu.com' , timeout=1)
# print(r.text)
# 下载文件
r = requests.get('https://i.bobopic.com/small/123161598.jpg')
print(r.content)
with open('./b.jpg', 'wb') as f:
    f.write(r.content)