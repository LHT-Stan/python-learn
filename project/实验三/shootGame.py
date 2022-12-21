# 添加装弹进度条
# 增加敌人躲避子弹功能
# 增加暴击功能
import sys


class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def show(self):
        print('角色名：', self.name)
        print('血量：', self.hp)


# 枪类
class Guns:
    def __init__(self, name, bullet):
        self.name = name
        self.bullet = bullet

    def __str__(self):
        return f'枪名：{self.name}，子弹：{self.bullet}'


# 战士类
class Warrior(Player):
    def __init__(self, name, hp=100):
        super().__init__(name, hp)
        self.gun = None

    # 装备武器
    def equip_gun(self, gun):
        self.gun = gun
        print(f'{self.name}装备武器成功，武器信息如下：{gun}')

    # 射击
    def shoot(self, enemy):
        if self.gun is None:
            print('没有枪')
        else:
            if self.gun.bullet > 0:
                self.gun.bullet -= 1
                print('射击成功，还剩', self.gun.bullet, '发子弹')
                enemy.hurt()
            else:
                print('子弹不足')
                # 输出一个缓慢增加的进度条
                import time
                for i in range(1, 21):
                    print('\r', end='')
                    print('装弹中：', end='')
                    print('#' * i, end='')
                    print(' ' * (20 - i), end='')
                    print(f'{i*5}%', end='')
                    time.sleep(0.1)
                print()
                self.reload(29)

    # 装弹
    def reload(self, num=30):
        for i in range(num+1):
            self.gun.bullet += 1
        print('装弹成功，还剩', self.gun.bullet, '发子弹')


# 敌人类
class Enemy(Player):
    def __init__(self, name, luck, hp=100):
        super().__init__(name, hp)
        self.luck = luck

    def hurt(self):
        # 产生一个1-10的随机数，如果小于luck值，敌人豁免伤害
        def dodge():
            import random
            return random.randint(1, 10)

        if self.hp > 0:
            print('敌人发动躲避技能')
            if dodge() < self.luck:
                print('\t敌人尝试躲避，躲避成功')
            elif dodge() == 9:
                if self.hp > 50:
                    self.hp -= 50
                    print('\t敌人躲避失败，受到暴击50点伤害，还剩', self.hp, '点血')
                else:
                    print('\t敌人躲避失败，受到暴击50点伤害，已死亡')
                    sys.exit(0)
            else:
                if self.hp > 5:
                    self.hp -= 5
                    print('\t敌人躲避失败，受到5点伤害，还剩', self.hp, '点血')
                else:
                    print('\t敌人躲避失败，受到5点伤害，已死亡')
                    sys.exit(0)
        else:
            print('敌人已死亡')
            sys.exit(0)


if __name__ == '__main__':
    # 创建战士
    w = Warrior('战士')
    w.show()
    # 创建敌人
    e = Enemy('敌人', 3)
    e.show()
    # 创建枪
    g = Guns('AK47', 5)
    # 装备枪
    w.equip_gun(g)
    # 射击
    print('发起一次射击')
    print('\t', end='')
    w.shoot(e)
    # 装弹
    w.reload(1)
    # 20次循环射击
    print('发起二十次射击')
    for i in range(30):
        print('\t', end='')
        w.shoot(e)
