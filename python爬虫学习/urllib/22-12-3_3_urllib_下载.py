import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# urllib.request.urlretrieve(url, filename)
# 两个参数，url代表的是下载的路径 filename文件的名字
# 在python中 可以写变量的名字，也可以写值
# 如：urllib.request.urlretrieve(url=url_page)
urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = 'http://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=Eminem&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=2552419945,1366176112&os=984693942,75249238&simid=3516929299,444922846&pn=2&rn=1&di=7169026086108397569&ln=1633&fr=&fmq=1670066510787_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=1e&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fp8.qhimg.com%252Ft01d486405c64124c1e.jpg%26refer%3Dhttp%253A%252F%252Fp8.qhimg.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1672658510%26t%3D2591ab70545271bfe97a55a129767bd8&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwzLDEsNiw0LDUsOCw3LDIsOQ%3D%3D'
urllib.request.urlretrieve(url=url_img, filename='Eminem.jpg')

# 下载视频
url_video = 'http://www.bilibili.com/7eb29a62-a8ca-4ecb-91ba-ff8f331dcc10'
urllib.request.urlretrieve(url=url_video, filename='video.mp4')










