
a = "".join(list(filter(str.isdigit, 'a1b2c3')))
print(a)

ori = input()
offset = 2
new = ''
for i in ori:
    new += chr((ord(i) - 2))
print(new)

