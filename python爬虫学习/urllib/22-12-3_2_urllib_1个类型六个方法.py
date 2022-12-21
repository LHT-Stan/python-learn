import urllib.request
# 总结一个类型HTTPResponse
# 六个方法read readline readlines getcode geturl getheaders
url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型六个方法
# response是HTTPResponse的类型
print(type(response))

# 按照一个字节一个字节的去读
# content = response.read()

# 读取5个字节
# content = response.reaa(5)

# 读取一行
content = response.readline()

# 一行一行读直到读完
content = response.readlines()

# 返回状态码，如果是200，逻辑没错
response.getcode()

# 返回url地址
response.geturl()

# 获取的一个状态信息
response.getheaders()

