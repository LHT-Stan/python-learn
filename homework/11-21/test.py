import pprint


txt = '''It is a bright cold day in April, and the clocks were striking thirteen.'''
count = {}
for c in txt:
    # setdefault的方法
    count.setdefault(c, 0)  # 确保每个字符有键值对
    count[c] += 1
    # get方法
    count[c] = count.get(c, 0) + 1

pprint.pprint(count)
