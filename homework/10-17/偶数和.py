numbers = 0
for i in range(101):
    if i & 1 == 0:
        numbers += i
print(numbers)
