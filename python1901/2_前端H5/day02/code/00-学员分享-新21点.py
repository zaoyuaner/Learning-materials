import random
import math


class ka_pai_21dian():

    beifen = {'1.1': '\x1b[31m♥A\x1b[0m', '2.1': '\x1b[31m♥2\x1b[0m', '3.1': '\x1b[31m♥3\x1b[0m',
              '4.1': '\x1b[31m♥4\x1b[0m', '5.1': '\x1b[31m♥5\x1b[0m', '6.1': '\x1b[31m♥6\x1b[0m',
              '7.1': '\x1b[31m♥7\x1b[0m', '8.1': '\x1b[31m♥8\x1b[0m', '9.1': '\x1b[31m♥9\x1b[0m',
              '10.1': '\x1b[31m♥10\x1b[0m', '11.1': '\x1b[31m♥J\x1b[0m', '12.1': '\x1b[31m♥Q\x1b[0m',
              '13.1': '\x1b[31m♥K\x1b[0m', '1.2': '\x1b[31m♦A\x1b[0m', '2.2': '\x1b[31m♦2\x1b[0m',
              '3.2': '\x1b[31m♦3\x1b[0m', '4.2': '\x1b[31m♦4\x1b[0m', '5.2': '\x1b[31m♦5\x1b[0m',
              '6.2': '\x1b[31m♦6\x1b[0m', '7.2': '\x1b[31m♦7\x1b[0m', '8.2': '\x1b[31m♦8\x1b[0m',
              '9.2': '\x1b[31m♦9\x1b[0m', '10.2': '\x1b[31m♦10\x1b[0m', '11.2': '\x1b[31m♦J\x1b[0m',
              '12.2': '\x1b[31m♦Q\x1b[0m', '13.2': '\x1b[31m♦K\x1b[0m', '1.3': '\x1b[30m♠A\x1b[0m',
              '2.3': '\x1b[30m♠2\x1b[0m', '3.3': '\x1b[30m♠3\x1b[0m', '4.3': '\x1b[30m♠4\x1b[0m',
              '5.3': '\x1b[30m♠5\x1b[0m', '6.3': '\x1b[30m♠6\x1b[0m', '7.3': '\x1b[30m♠7\x1b[0m',
              '8.3': '\x1b[30m♠8\x1b[0m', '9.3': '\x1b[30m♠9\x1b[0m', '10.3': '\x1b[30m♠10\x1b[0m',
              '11.3': '\x1b[30m♠J\x1b[0m', '12.3': '\x1b[30m♠Q\x1b[0m', '13.3': '\x1b[30m♠K\x1b[0m',
              '1.4': '\x1b[30m♣A\x1b[0m', '2.4': '\x1b[30m♣2\x1b[0m', '3.4': '\x1b[30m♣3\x1b[0m',
              '4.4': '\x1b[30m♣4\x1b[0m', '5.4': '\x1b[30m♣5\x1b[0m', '6.4': '\x1b[30m♣6\x1b[0m',
              '7.4': '\x1b[30m♣7\x1b[0m', '8.4': '\x1b[30m♣8\x1b[0m', '9.4': '\x1b[30m♣9\x1b[0m',
              '10.4': '\x1b[30m♣10\x1b[0m', '11.4': '\x1b[30m♣J\x1b[0m', '12.4': '\x1b[30m♣Q\x1b[0m',
              '13.4': '\x1b[30m♣K\x1b[0m'}
    ka_pai = {'1.1': '\x1b[31m♥A\x1b[0m', '2.1': '\x1b[31m♥2\x1b[0m', '3.1': '\x1b[31m♥3\x1b[0m',
              '4.1': '\x1b[31m♥4\x1b[0m', '5.1': '\x1b[31m♥5\x1b[0m', '6.1': '\x1b[31m♥6\x1b[0m',
              '7.1': '\x1b[31m♥7\x1b[0m', '8.1': '\x1b[31m♥8\x1b[0m', '9.1': '\x1b[31m♥9\x1b[0m',
              '10.1': '\x1b[31m♥10\x1b[0m', '11.1': '\x1b[31m♥J\x1b[0m', '12.1': '\x1b[31m♥Q\x1b[0m',
              '13.1': '\x1b[31m♥K\x1b[0m', '1.2': '\x1b[31m♦A\x1b[0m', '2.2': '\x1b[31m♦2\x1b[0m',
              '3.2': '\x1b[31m♦3\x1b[0m', '4.2': '\x1b[31m♦4\x1b[0m', '5.2': '\x1b[31m♦5\x1b[0m',
              '6.2': '\x1b[31m♦6\x1b[0m', '7.2': '\x1b[31m♦7\x1b[0m', '8.2': '\x1b[31m♦8\x1b[0m',
              '9.2': '\x1b[31m♦9\x1b[0m', '10.2': '\x1b[31m♦10\x1b[0m', '11.2': '\x1b[31m♦J\x1b[0m',
              '12.2': '\x1b[31m♦Q\x1b[0m', '13.2': '\x1b[31m♦K\x1b[0m', '1.3': '\x1b[30m♠A\x1b[0m',
              '2.3': '\x1b[30m♠2\x1b[0m', '3.3': '\x1b[30m♠3\x1b[0m', '4.3': '\x1b[30m♠4\x1b[0m',
              '5.3': '\x1b[30m♠5\x1b[0m', '6.3': '\x1b[30m♠6\x1b[0m', '7.3': '\x1b[30m♠7\x1b[0m',
              '8.3': '\x1b[30m♠8\x1b[0m', '9.3': '\x1b[30m♠9\x1b[0m', '10.3': '\x1b[30m♠10\x1b[0m',
              '11.3': '\x1b[30m♠J\x1b[0m', '12.3': '\x1b[30m♠Q\x1b[0m', '13.3': '\x1b[30m♠K\x1b[0m',
              '1.4': '\x1b[30m♣A\x1b[0m', '2.4': '\x1b[30m♣2\x1b[0m', '3.4': '\x1b[30m♣3\x1b[0m',
              '4.4': '\x1b[30m♣4\x1b[0m', '5.4': '\x1b[30m♣5\x1b[0m', '6.4': '\x1b[30m♣6\x1b[0m',
              '7.4': '\x1b[30m♣7\x1b[0m', '8.4': '\x1b[30m♣8\x1b[0m', '9.4': '\x1b[30m♣9\x1b[0m',
              '10.4': '\x1b[30m♣10\x1b[0m', '11.4': '\x1b[30m♣J\x1b[0m', '12.4': '\x1b[30m♣Q\x1b[0m',
              '13.4': '\x1b[30m♣K\x1b[0m'}
    player = []
    name1_pai = []
    name2_pai = []
    gai_lv = {}
    gai_lv2 = {}
    zhuang = 0
    xian = 0
    ping = 0
    # 模式选择
    def main(self):
        patterm = input("单人模式还是双人模式？ d/s")
        if patterm == 's':
            self.double_mode()
        if patterm == 'd':
            self.ai_mode()
        else:
            print("\033[31m输入有误\033[0m")

    # 双人模式
    def double_mode(self):
        # name1 = input("玩家1的名字:")
        # name2 = input("玩家2的名字:")
        name1 = '赌方'
        name2 = '庄家'
        self.player.append(name1)
        self.player.append(name2)
        while True:
            # 初始化
            self.ka_pai.update(self.beifen)
            self.name1_pai = []
            self.name2_pai = []

            print("\033[1;0m游戏开始\033", name1, "vs", name2)
            # 游戏开始，玩家1发牌
            score1 = self.play_AI(name1)
            print()
            # 玩家1结束后 玩家2开始
            score2 = self.play_AI(name2)
            print()

            # 谁赢了
            f = self.determine_winner(name1, name2, score1, score2)
            # f = {name1:{score1:True},name2:{score2:True}}
            for i in f:
                if i not in self.gai_lv.keys():
                    self.gai_lv[i] = 1
                elif i in self.gai_lv.keys():
                    self.gai_lv[i] += 1
            # 多少点数获胜的概率
            for key,value in self.gai_lv.items():
                self.gai_lv2[key] = math.ceil(value/sum(self.gai_lv.values())*100)
            print(dict(sorted(self.gai_lv2.items(), key=lambda x: x[1], reverse=True)))
            print('赌：',self.xian,'庄：',self.zhuang,'平局：',self.ping)

            go_no = input("\033[34m你想再玩一次吗? 回车继续/no \n")
            if go_no == "no":
                break


    # AI 单人模式
    def ai_mode(self):
        name1 = input("玩家1的名字:")
        name2 = 'AI'
        self.player.append(name1)
        self.player.append(name2)
        while True:
            self.ka_pai.update(self.beifen)
            self.name1_pai = []
            self.name2_pai = []

            print("\033[1;0m游戏开始\033", name1, "vs", name2)
            score2 = self.play_AI(name2)
            print("AI 抽卡完毕\n")
            score1 = self.play_turn(name1)
            print()

            self.determine_winner(name1, name2, score1, score2)
            go_no = input("\033[34m你想再玩一次吗? 回车继续/no\033[0m \n")
            if go_no == "no":
                break



    # 玩家
    def play_turn(self, name):
        print("==========[ \033[1;0m当前玩家:\033[0m", " \033[1;34m{}\033[0m ]==========".format(name))
        # 目前点数
        num = 0
        # 发牌
        while True:
            num += self.deal_card(name)
            # 打印点数
            print("点数:", num)
            if num <= 21:
                # 是否继续要牌
                chose = input("还要不要牌? y/n")
                if chose == "n":
                    return num
            elif num > 21:
                # 玩家1
                if self.player.index(name) == 0 and int(1) in self.name1_pai:
                    self.name1_pai.remove(1)
                    self.name1_pai.append('1')
                    num -= 10
                    print("\033[31m点数超过21点，A牌将算做\033[0m", "\033[33m1\033[0m", "\033[31m点", "\n",
                          "\033[1;31m现点数：{}\033[0m".format(num))
                    chose = input("还要不要牌? y/n")
                    if chose == "n":
                        return num

                # 玩家2
                elif self.player.index(name) == 1 and int(1) in self.name1_pai:
                    self.name2_pai.remove(1)
                    self.name2_pai.append('1')
                    num -= 10
                    print("\033[31m点数超过21点，A牌将算做\033[0m", "\033[33m1\033[0m", "\033[31m点", "\n",
                          "\033[1;31m现点数：{}\033[0m".format(num))
                    chose = input("还要不要牌? y/n")
                    if chose == "n":
                        return num
                else:
                    print("\033[31m爆点了！\033[0m")
                    return '爆'

    # AI
    def play_AI(self, name):
        print("==========[ \033[1;0m当前玩家:\033[0m", " \033[1;34m{}\033[0m ]==========".format(name))
        num = 0
        while True:
            num += self.deal_card(name)
            # 现卡牌 里加起来不超过21的牌
            ok = []
            for ka in self.ka_pai.keys():
                if num + int(eval(ka)) <= 21:
                    ok.append(ka)
            # print('库',len(ka_pai),'安全',len(ok))
            # AI 抽卡概率，安全的卡/牌库*100 向上取整
            AI_card = math.ceil(len(ok) / len(self.ka_pai) * 100)
            # print('点数：', num, '概率：', AI_card)
            if num <= 21:
                # 随机概率抽卡
                if AI_card > 50:
                    pass
                else:
                    return num
            elif num > 21:
                # 超过21点 判断有没有 A
                if int(1) in self.name2_pai:
                    self.name2_pai.remove(1)
                    self.name2_pai.append('1')
                    num -= 10
                else:
                    return '爆'

    # 发牌
    def deal_card(self, name):
        # 随机获得卡牌
        ka_list = list(self.ka_pai.keys())
        nums = random.choice(ka_list)
        num = int(eval(nums))
        # 保存卡牌，如何爆点了有 A牌的话可以算 1 点
        if self.player.index(name) == 0:
            self.name1_pai.append(num)
        elif self.player.index(name) == 1:
            self.name2_pai.append(num)
        # 删除牌库
        self.ka_pai.pop(nums)
        # 打印结果
        self.print_card(name, nums)
        # 大于10的特殊牌按10点算
        if num >= 10:
            return 10
        # 如果是A 默认11点
        elif num == 1:
            return 11
        elif num < 10:
            return int(num)

    # 特殊A J Q K 牌显示
    def print_card(self, name, nums):
        # 如果牌是1、11、12、13，则输出A、J、Q、K
        if name != 'AI':
            print(name, "你的牌是", self.beifen[nums])
        # AI 不显示
        elif name == 'AI':
            print(name, '抽了一张卡牌')

    # 结算输赢
    def determine_winner(self, name1, name2, score1, score2):
        print("{:<8}:{}点 \n{:<8}:{}点".format(name1, score1, name2, score2))
        if score1 == '爆': score1 = -1
        if score2 == '爆': score2 = -1
        if score1 == score2:
            print("\033[1;0m {} 和 {} 平局!\033[0m".format(name1, name2))
            self.ping += 1
        elif score1 > score2:
            print("\033[1;35m玩家", name1, "赢了!\033[0m")
            self.xian += 1
        elif score1 < score2:
            print("\033[1;35m玩家", name2, "赢了!\033[0m")
            self.zhuang += 1
        return score1,score2


if __name__ == "__main__":
    r = ka_pai_21dian()
    r.main()
