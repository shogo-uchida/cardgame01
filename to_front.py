



import random
import back
from functools import partial
from browser import document
from browser import timer
from browser.template import Template



def start_game(ev):
	document['start'].text = 'start'
	show_card()
	show_point()
	document['whichWin'].text = ''

def show_card():
	player0 = document['player0']
	player1 = document['player1']
	player2 = document['player2']

	pc0 = document['pc0']
	pc1 = document['pc1']
	pc2 = document['pc2']

	player0.text = str(player_hand.cards[0])
	player1.text = str(player_hand.cards[1])
	player2.text = str(player_hand.cards[2])

	pc0.text = str(pc_hand.cards[0])
	pc1.text = str(pc_hand.cards[1])
	pc2.text = str(pc_hand.cards[2])


def show_point():
	player_point = document['playerPoint']
	pc_point = document['pcPoint']	
	
	player_point.text = player_hand.point
	pc_point.text = pc_hand.point	


def select0(ev):
	player_card = player_hand.choose_card(0)
	select(player_card)
	#timer.set_timeout(select(player_card), 3000)
	# dunno why this doesnt work!
	#module browser.timer line 13, in f   has some error

def select1(ev):
	player_card = player_hand.choose_card(1)
	select(player_card)
	#timer.set_timeout(select(player_card), 3000)
	# dunno why this doesnt work!

def select2(ev):
	player_card = player_hand.choose_card(2)
	select(player_card)
	#timer.set_timeout(select(player_card), 3000)
	# dunno why this doesnt work!

def select(player_card):
	pc_num = random.randrange(0,3)
	pc_card = pc_hand.choose_card(pc_num)
	if pc_num == 0:
		Template(document["pc0"]).render(select="selected")
	if pc_num == 1:
		Template(document["pc1"]).render(select="selected")
	if pc_num == 2:
		Template(document["pc2"]).render(select="selected")
# make class with variable in HTML and we can change it!!
# for player, I used javascript. (script.js)

	which_win = back.compare(player_card, pc_card)
	if not type(which_win) == str:
		which_win = 'even'
	document['whichWin'].text = which_win
	show_point()
	loser_judge()


def next_round(ev):
	show_card()
#	Template(document.get(selector='.pc_item')).render(select="")
#class="hoge"の要素をリスト形式で取得

def loser_judge():
	judge = back.loser_judge(player_hand, pc_hand)
	if judge == 0:
		document['whichWin'].text = 'game over, you lost, press reset to continue'
		document['start'].text = 'reset'
		back.main()
		main()

	elif judge == 1:
		document['whichWin'].text = 'game over, you won, press reset to continue'
		document['start'].text = 'reset'
		back.main()
		main()


def main():
	global player_hand	
	global pc_hand	

	player_hand = back.player_hand # this should be an array of card
	pc_hand = back.pc_hand



main()

start_btn = document["start"]
start_btn.bind('click', start_game)


#document.get(name='hoge') #name="hoge"の要素をリスト形式で取得
select_btn0 = document['player0'] 
select_btn0.bind('click', select0)

select_btn1 = document['player1']
select_btn1.bind('click', select1)

select_btn2 = document['player2'] 
select_btn2.bind('click', select2)

start_btn = document["next"]
start_btn.bind('click', next_round)

