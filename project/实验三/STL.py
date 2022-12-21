# 要求完成学生（student）、组长（leader）、教师（teacher）类的定义，并创建实例对象，模拟各种行为。
# 具体需求：
# （1）学生：姓名、年龄、学号；吃饭、睡觉、学习
# （2）组长：姓名、年龄、学号、职务；吃饭、睡觉、学习、管理
# （3）教师：姓名、年龄、职务；吃饭、睡觉、教学、管理
# 编程过程：
# （1）定义类，添加属性和方法；
# （2）根据前述需求，考虑如何设计继承关系，是否会用到多继承等；
# （3）入口函数：测试程序，分别创建实例对象：小明、王组长、张老师，调用各自方法。

# 由于学生、组长、教师都有姓名、年龄等属性，吃饭、睡觉等方法，所以可以定义一个父类抽出公有的属性和方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + ' 在吃莽莽')

    def sleep(self):
        print(self.name + ' 在睡觉觉')


# 定义学生类，继承自Person类
class Student(Person):
    def __init__(self, name, age, studentNumber):
        super().__init__(name, age)
        self.studentNumber = studentNumber

    def learn(self):
        print(self.name + ' 在努力学习ing....')


# 定义组长类，继承自Student类
class Leader(Student):
    def __init__(self, name, age, studentNumber, position):
        super().__init__(name, age, studentNumber)
        self.position = position

    def manage(self):
        print(self.name + ' 在管理ing....')


# 定义教师类，继承自Person类
class Teacher(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def teach(self):
        print(self.name + ' 在教学ing....')

    def manage(self):
        print(self.name + ' 在管理ing....')


# 入口函数
def main():
    # 创建实例对象
    stu1 = Student('stu1', 18, 'S001')
    stu2 = Leader('stu2', 19, 'S002', '组长')
    tea = Teacher('tea', 25, '老师')

    # 调用stu1的方法
    stu1.eat()
    stu1.sleep()
    stu1.learn()
    # 调用stu2的方法
    stu2.eat()
    stu2.sleep()
    stu2.learn()
    stu2.manage()
    # 调用Teacher方法
    tea.eat()
    tea.sleep()
    tea.teach()
    tea.manage()


main()
