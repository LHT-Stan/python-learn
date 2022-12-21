class Dog:
    name = '狗'  # 定义属性

    def eat(self, food):  # 在调用时会自动把对象传入参数，self自己
        print(f"吃{food}")


dog1 = Dog()
print(dog1.name)
dog1.eat("shit")
