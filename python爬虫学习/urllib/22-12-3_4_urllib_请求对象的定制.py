import urllib.request

# 注意此处多了一个s
url = 'https://www.mingorfang.top/post/2b395545.html'
# url的组成
# https://www.baidu.com/s?wd=????
# http/https           www.baidu.com     80/443       s     wd=????      #
#     协议                   主机          端口号       路径     参数        锚点
# http 80
# https 443
# mysql 3306

# 由于此处加了s需要UA验证，所以获取UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}
# 又因为urlopen不能直接传入headers参数，故此需要包装成request对象，详情见urlopen说明
# 定制请求对象
request = urllib.request.Request(url=url, headers=headers)  # 包装request，因为内部参数不止两个，所以需要使用关键字传参的方式传入，详情见内部源码
# 获取响应
response = urllib.request.urlopen(request)

# 解码 decode('编码的格式')
content = response.read().decode('utf-8')
print(content)



