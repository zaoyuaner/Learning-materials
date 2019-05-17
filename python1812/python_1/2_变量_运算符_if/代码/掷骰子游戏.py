import random
import time


def get_dice():
	return random.randint(1, 7)


def the_open(player_dice, computer_dice):
	print
	'双方开：'
	time.sleep(1)
	print
	'玩家：' + str(player_dice)
	time.sleep(1)
	print
	'电脑：' + str(computer_dice)
	time.sleep(1)


def every_game(player_money, computer_money):
	print
	'Get Ready~~~'
	time.sleep(1)
	print
	'Go!'
	time.sleep(2)
	print
	"双方筹码："
	print
	'玩家：' + str(player_money)
	print
	'电脑：' + str(computer_money)
	time.sleep(2)
	print
	'玩家掷点：',
	time.sleep(1)
	player_dice = get_dice()
	print
	'您得到的点数为' + str(player_dice)
	time.sleep(2)
	print
	'电脑掷点：',
	time.sleep(1)
	computer_dice = get_dice()
	print
	'电脑掷点完毕！'
	time.sleep(1)
	result = raw_input('玩家方先下注，是否下注？[y/N]')
	if result.lower() == 'y':
		while True:
			player_bets = input('选择下注范围：[1-{0}]'.format(player_money))
			if player_bets >= 1 and player_bets <= player_money:
				break
		print
		'玩家下注{0}'.format(player_bets)
		time.sleep(1)
		print
		'电脑思考中...',
		time.sleep(2)
		if random.choice('yn') == str('y'):
			computer_bets = random.randint(1, computer_money)
			print
			'电脑下注{0}'.format(computer_bets)
			time.sleep(1)
			the_open(player_dice, computer_dice)
			if player_dice > computer_dice:
				print
				'玩家胜！玩家赢得筹码{0}'.format(computer_bets)
				player_money += computer_bets
				computer_money -= computer_bets
			elif player_dice == computer_dice:
				print
				'平局！双方收回各自筹码！'
			else:
				print
				'电脑胜！玩家输掉筹码{0}'.format(player_bets)
				player_money -= player_bets
				computer_money += player_bets
		else:
			print
			'电脑放弃下注！玩家收回自己的筹码！'
			time.sleep(1)
			the_open(player_dice, computer_dice)
	else:
		print
		'玩家放弃下注，本局放弃！'
		time.sleep(1)
		the_open(player_dice, computer_dice)
	return [player_money, computer_money]


def play_game():
	print
	'游戏开始！'
	player_money = 100
	computer_money = 100
	time.sleep(1)
	while player_money != 0 and computer_money != 0:
		money_list = every_game(player_money, computer_money)
		player_money = money_list[0]
		computer_money = money_list[1]
	if player_money == 0:
		print
		'You Lose!'
	else:
		print
		'You Win!'


if __name__ == '__main__':
	play_game()