'''

This is the game Shogo makes
the rule is following
There are 30 cards with the range of 1 to 10
Each card has rock, scissors or paper
2 players play the game, each of them has 3 card.
they can see all the cards no matter who has
each tern, they have to choose one card from their hands
if they win the rock-paper-scissors, they can damage the opponent with the number with it
each of them have 15 points from the beginning
the one who lose all the points lose.

'''


from tkinter import *
import random
import back
from functools import partial
# when using tkinter to take argment

def continue_command():
    back.main()
    show_card(back.player_hand, back.pc_hand)
    show_point(back.player_hand, back.pc_hand)
    first_column(' ',4 , column = 0, cha_text = '           got it             ')
    first_column(' ', 5, 1, 'b')
    first_column(' ', 5, 2, 'c')

def finish_command():
    quit()

def loser_judge_command(player_hand, pc_hand):
    judge = back.loser_judge(player_hand, pc_hand)
    if judge == 0 or judge == 1:
        if judge == 0:
            first_column('YOU LOSE', 3)
        elif judge == 1:
            first_column('YOU WIN', 3)

        first_column('do you wanna play again?', 4)
        continue_button = Button(window, text = 'continue', command = continue_command)
        continue_button.grid(row = 5, column = 1)
        finish_button = Button(window, text = 'finish', command = finish_command)
        finish_button.grid(row=5, column=2)

def choose_hand_command(player_hand, pc_hand, index):
    pc_card = pc_hand.choose_card(random.randrange(0,3))
    player_card = player_hand.choose_card(index)
    back.compare(player_card, pc_card)
    show_point(player_hand, pc_hand)
    show_card(player_hand, pc_hand)
    loser_judge_command(player_hand, pc_hand)


def show_card(player_hand, pc_hand):

    for i in range(3): # pc hand
        card = Label(window, text = pc_hand.cards[i], width=20)
#                      command = partial(choose_hand_command, back.pc_hand, i))
        card.grid(row=1, column=i+1)
    for j in range(3):
        card = Button(window, text = player_hand.cards[j], width=20,
                      command = partial(choose_hand_command, back.player_hand,
                                        back.pc_hand, j))
        card.grid(row=3, column=j+1)

def show_point(player_hand, pc_hand):
    pc_hand_point = Label(window, text=pc_hand.point, width=10)
    pc_hand_point.grid(row=1, column=4)
    player_hand_point = Label(window, text=player_hand.point, width=10)
    player_hand_point.grid(row=3, column=4)

def first_column(text, row, column = 0, cha_text = 0):
#    text = Label(window, text=text)
#    text.grid(row=row, column=0)

#    var = StringVar()
#    var.set(text)
    label = Label(window, text=text)
    label.grid(row=row, column=column)

    if cha_text != 0:
        label.config(text = cha_text)
        label.grid(row=row, column=column)




window = Tk()
window.wm_title('Rock paper scissors advanced')

show_card(back.player_hand, back.pc_hand)

l0 = Label(window, text = 'the game of advanced rock paper scissors')
l0.grid(row = 0, column = 0)

first_column('pc card', 1)

first_column('time', 2)

first_column('your card', 3)

first_column(' ', 4)
first_column(' ', 5)

show_point(back.player_hand, back.pc_hand)



window.mainloop()

























