import requests
import parsel
import csv
import time

csv_qnc = open('去哪儿数据分析.csv', mode='a', encoding='utf-8', newline='')
csv_write = csv.writer(csv_qnc)
csv_write.writerow(['地点', '短评', '出发时间', '天数', '人均费用', '人物', '玩法', '浏览量', '详情页'])
# (1)向目标发送请求
for page in range(1, 201):
    url = f'https://travel.qunar.com/travelbook/list.htm?page={page}&order=hot_heat'
    # 请求头：把python伪装成浏览器 给服务器发送请求
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
    }
    # <Response [200]>
    # 请求成功

    # (2)获取数据
    response = requests.get(url=url, headers=headers)
    # 获取数据网页源代码
    # print(response.text)
    print(page)
    # (3)解析网页（re正则表达式，css选择器，xpath，bs4，json）
    # html_data:字符串
    selector = parsel.Selector(response.text)
    print(selector)
    # 现在把这个字符串变成一个对象
    #::attr(href) 获取属性格式
    # 第一次提取，返回值也是对象
    # id选择器可以直接用#定位
    url_list = selector.css('body > div.qn_mainbox > div > div.left_bar > ul > li > h2 > a::attr(href)').getall()
    for detail_id in url_list:
        print(detail_id)
        # 提取每一详情页的id
        detail_id = detail_id.replace('/youji/', '')
        detail_url = 'https://travel.qunar.com/travelbook/note/' + detail_id
        # print(detail_id)
        # 向详情页面发送网络请求
        response_1 = requests.get(detail_url)
        # 获取数据 网页源代码
        print(response_1.text)
        # 提取数据
        selector_1 = parsel.Selector(response_1.text)
        # 获取标题
        title = selector_1.css('div.b_cover > div.b_crumb > p > a:nth-child(3)::text').get()
        # 短评
        comment = selector_1.css('.title.white::text').get()
        # 出发日期
        date = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p > span.data::text').get()
        # 天数
        day = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p > span.data::text').get()
        # 人均费用
        money = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howmuch > p > span.data::text').get()
        # 人物
        person = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p > span.data::text').get()
        # 玩法
        play_list = selector_1.css(
            '#js_mainleft > div.b_foreword > ul > li.f_item.how > p > span.data > span::text').getall()
        # 浏览量
        look = selector_1.css('.view_count::text').get()
        print(title, comment, date, day, money, person, play_list, look, detail_url)
        csv_write.writerow([title, comment, date, day, money, person, play_list, look, detail_url])
