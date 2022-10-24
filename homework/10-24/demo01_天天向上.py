# 以第1天的能力值为基数,好好学习每天提升5%，不学习下降5%
# 那么一年下来每天努力和每天放任的能力值差多少?
# 如果改为提升和下降1%呢?
# 如果平时努力可提升1%，双休日放任下降1%呢?
from math import pow

base = 1
factor = 0.01
up = 365/7
dayUp = pow(base + factor, up*5)
dayDown = pow(base - factor, up*2)
print(f"每天努力的：{dayUp:.2f}; 每天放松：{dayDown:.2f}")

