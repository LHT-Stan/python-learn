num1, num2 = map(int, input("请输入两个数字：").split())
m = max(num1, num2)
n = min(num1, num2)
r = m % n
while r != 0:
    m = n
    n = r
    r = m % n
print(num1, "和", num2, "的最大公约数为", n)
