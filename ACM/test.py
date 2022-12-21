n, m = map(int, input().split())
tea = {}
stu = {}
tea1 = []
for i in range(n):
    s1, s2 = input().split()
    tea1.append(s1)
    tea.setdefault(s1, s2)
for i in range(m):
    s1, s2 = input().split()
    stu2 = {s1: s2}
    stu.update(stu2)

res = True
for i in range(len(tea1)):
    if tea.get(tea1[i]) != stu.get(tea1[i]):
        print(tea1[i] + " " + stu.get(tea1[i]))
        res = False
    if res:
        print("ni de nei rong zhe li you wen ti ba?")



