import time
start = time.time()
for i in range(5, 0, -1):
    print(f"\r倒计时{i}秒！", end="")
    time.sleep(1)
print("\r倒计时结束！")
end = time.time()
print('运行时间: %ss' % (end - start))
    