import urllib.request
import urllib.parse

# 要求爬取https://www.baidu.com/s?wd=周杰伦
# 由于url中有中文，而在爬取中会报错，所以需要特殊处理，见下方

url = 'https://www.baidu.com/s?wd='

# 定制UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

# 将汉字转为unicode编码的格式
# 需要依赖于urllib.parse包
name = urllib.parse.quote('周杰伦')
url = url + name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 发送请求，获取响应
response = urllib.request.urlopen(request)
# 获取响应内容，并转换字符集
content = response.read().decode('utf-8')

print(content)





