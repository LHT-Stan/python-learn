import time
for i in range(10):
    print("\r"+"■"*i, sep="", end="")
    time.sleep(0.2)
print("\n下载完成")
