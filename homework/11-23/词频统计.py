# 三国演义 人物出场统计
import jieba

f = open("E:/Projects/Pycharm-Projects/三国演义.txt", "r", encoding='utf-8')
# 使用with,不需要关闭,close.可以自动的执行关闭文件,出现异常都能正常的自动关闭并保存
with open("E:/Projects/Pycharm-Projects/三国演义.txt", "r", encoding='utf-8') as f:
    txt = f.read()  # read 一次性读取全部内容，保存为字符串

words = jieba.lcut(txt)  # 中文分词保存为列表
excludes = ['却说', '二人', '不可', '将军', '丞相', '荆州', '不能', '如此', '如何', '商议', '主公', '军士', '左右', '军马', '引兵', '次日'
            , '如此', '大喜', '天下', '于是', '今日', '东吴', '不敢', '魏兵', '陛下', '人马', '不知', '一人', '都督', '汉中']
# 统计
count = {}  # 初始化统计结构
# 统计词频，遍历
for word in words:
    if len(word) == 1 or word in excludes:
        continue
    elif word == "孔明" or word == "孔明曰" or word == "卧龙" or word == "诸葛丞相":
        rword = "诸葛亮"
    elif word in ["玄德", "玄德曰", "皇叔", "玄德公"]:
        rword = "刘备"
    elif word in ["孟德", "孟德曰", "曹丞相", "曹贼", "阿蛮"]:
        rword = "曹操"
    elif word in ["关公", "云长", "云长曰", "关将军"]:
        rword = "关羽"
    else:
        rword = word
    count[rword] = count.get(rword, 0) + 1
# 排序
items = list(count.items())  # 获取字典的项，保存为列表，以元组形式
items.sort(key=lambda x: x[1], reverse=True)  # 按词频倒序排序输出
# 打印前十项
for i in range(10):
    word, times = items[i]
    print(f"{word}\t{times}")


