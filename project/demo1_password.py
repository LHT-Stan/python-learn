def main():
    # 终止器
    count = 0
    # 密码强度
    password_strength = 0
    while count < 4:
        count += 1
        password = input("请输入密码:")
        if count == 4:
            print("已超过最大尝试次数，程序结束")
            return
        if len(password) < 8:
            print("密码长度要求至少8位！")
            if password.isalpha():
                password_strength = -2
                check_password_strength(password_strength)
                continue
            if password.isdigit():
                password_strength = -3
                check_password_strength(password_strength)
                continue
        elif len(password) >= 8:
            password_strength = 1
            # 判断密码是否只有字母
            if password.isalpha():
                password_strength = -1
                check_password_strength(password_strength)
            elif not check_number(password):
                check_password_strength(password_strength)
        # 判断密码是否包含数字和字母
        if check_Case(password):
            check_password_strength(4)
            return
        elif check_letter(password) and check_number(password):
            password_strength = 3
            check_password_strength(password_strength)
            return
        elif check_number(password):
            password_strength = 2
            check_password_strength(password_strength)


# 密码强度检测
def check_password_strength(password_strength):
    # 密码强度对照表
    if password_strength == 1:
        print("1.当前密码强度'*'弱,密码强度不合格")
        print("2.密码以满足有8位，请加入字母和数字组合增强密码强度")
        return False
    elif password_strength == 2:
        print("1.当前密码强度'***'中等,密码强度不合格")
        print("2.密码以满足有8位、有数字，请加入字母组合增强密码强度")
        return False
    elif password_strength == -1:
        print("1.当前密码强度'***'中等,密码强度不合格")
        print("2.密码以满足有8位、有字母，请加入数字组合增强密码强度")
        return False
    elif password_strength == -2:
        print("1.当前密码强度'***'中等,密码强度不合格")
        print("2.密码已有字母，请加入数字组合增强密码强度")
        return False
    elif password_strength == -3:
        print("1.当前密码强度'***'中等,密码强度不合格")
        print("2.密码已有数字，请加入字母组合增强密码强度")
        return False
    elif password_strength == 3:
        print("!!!恭喜，当前密码强度'******'强,密码强度合格")
    elif password_strength == 4:
        print("!!!恭喜，解锁隐藏彩蛋")
        print("!!!密码满足8位且同时包含数字、字母、大小写")
        print("密码强度达到：**********")


# 判断密码是否有数字
def check_number(password):
    is_num = False
    for i in password:
        if i.isdigit():
            is_num = True
    return is_num


# 判断密码是否有字母
def check_letter(password):
    is_letter = False
    for i in password:
        if i.isalpha():
            is_letter = True
    return is_letter


# 判断是否同时有大小写
def check_Case(password):
    is_case = False
    one = False
    two = False
    for i in password:
        if i.islower():
            one = True
        if i.isupper():
            two = True
    if two and one:
        is_case = True
    return is_case


main()
