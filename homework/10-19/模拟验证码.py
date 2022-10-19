import random
s = ''
nums = random.randint(1, 6)
strs = 6 - nums
for i in range(nums):
    num = random.randint(0, 9)
    s += str(num)
if strs == 0:
    print(s)
else:
    for i in range(strs):
        str = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        s += str
    print(s)
