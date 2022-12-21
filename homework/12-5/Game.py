class Game:
    top_score = 0

    def __init__(self, name):
        self.player_name = name

    def __str__(self,):
        return "{}".format(self.player_name)

    def start_game(self):
        print(f"{self.player_name}开始了游戏......")

    @classmethod
    def show_top_score(cls):
        print(f"历史最高分为：{cls.top_score}")

    @staticmethod
    def show_help():
        print("消消乐：3个及以上成排消掉")


game = Game("白夜")
game.start_game()
game.show_top_score()
game.show_help()

