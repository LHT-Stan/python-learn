# 判断密码不能小于8位
def length(password):
    return len(password) >= 8
# 判断密码需要包含数字
def number(password):
    has_number = False
    for c in password:
        if c.isnumeric():
            has_number = True
            break
    return has_number
# 判断密码需要包含字母
def length (password):
    has_letter = False
    for c in password:
        if c.isalpha():
            has_letter = True
            break
    return has_letter
frequency = 4





while frequency > 0:
    password = input('请输入密码：')
    # 设置密码强度
    strength = 0
    if letter(password):
        strength += 1
    else:
        print('密码长度至少8位！')
    if number(password):
        strength += 1
    else:
        print('密码要求包含数字！')
    if letter(password):
        strength += 1
    else:
        print('密码要求包含字母！')
    if strength == 3:
        print('恭喜！密码强度合格！')
        break
    else:
        print('密码强度不合格！')
        frequency -= 1