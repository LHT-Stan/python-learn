while True:
    try:
        current_period = float(input("当期股价算术平均数："))
        base_period = float(input("基期股价算术平均数："))
        spi = round(current_period/base_period, 4)      # 保留4位小数，以便化为百分数时保留2位小数
    # 输入了非数字
    except ValueError:
        print("输入错误，请输入数字")
    # 基期股价为0
    except ZeroDivisionError:
        print("基期股价不能为0")
    else:
        # 以百分数形式输出，并保留2位小数
        print(f"股价指数为：{spi:.2%}")
    finally:
        choice = input("输入Y继续，输入其他结束")
        if choice not in ('Y', 'y'):
            break

# 使用Python异常处理的语法编写代码，实现股票价格指数<股票价格指数spi=（当期股价算术平均数current_period÷基期股价算术平均数base_period）×100%>的计算和显示。要求如下：
#
# （1）当前股价算术平均数和基期股价算术平均数由键盘输入；（2）若用户输入非数字或基期股价算术平均数为0，可以分别打印出错误提示；（3）若用户输入的数值正常，计算并打印出spi结果（保留2位小数）；（4）程序可以循环运行，直到用户选择终止程序。
