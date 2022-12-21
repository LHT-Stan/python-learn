import random as r
# randrange是左闭右开
a = [r.randrange(2, 101, 2) for i in range(10)]
a.insert(0, 0)
a.insert(len(a), 66)
# a.append(66)
print(a)
a.sort(reverse=True)
print(a[2:5])
x, y, z = a[2:5]
print(x, y, z)
r.shuffle(a)
a.remove(max(a))
a.pop()

