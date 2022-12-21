# 定义角色类
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return self.name + ': ' + str(self.health)


# 定义战士类，继承自Character类
class Warrior(Character):
    def __init__(self, name, health=100, gun=None):
        super().__init__(name, health)
        self.gun = gun

    def shoot(self, enemy):
        if self.gun.bullets > 0:
            enemy.health -= 5
            self.gun.bullets -= 1
            print(self.name + ' shoots ' + enemy.name + ' and hits!')
        else:
            print(self.name + ' tries to shoot, but has no bullets!')


# 定义枪弹类
class Gun:
    def __init__(self, bullets=0):
        self.bullets = bullets

    def __str__(self):
        return 'bullets: ' + str(self.bullets)


# 入口函数
def main():
    # 创建角色和枪弹对象
    tom = Warrior('Tom')
    jerry = Character('Jerry')
    gun = Gun(10)

    # 模拟装弹
    print(tom.name + ' reloads the gun with ' + str(gun))

    # 模拟射击
    tom.shoot(jerry)

    # 模拟杀伤敌人
    tom.shoot(jerry)
    tom.shoot(jerry)

    # 模拟子弹用完
    tom.shoot(jerry)
    tom.shoot(jerry)


if __name__ == '__main__':
    main()
