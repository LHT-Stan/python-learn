members = [{'name': '张三', 'age': 68}, {'name': '李四', 'age': 81}, {'name': '王五', 'age': 65},
           {'name': '赵六', 'age': 68}]

result = sorted(members, key=lambda x: (-x['age'], x['name']))

print(result)
