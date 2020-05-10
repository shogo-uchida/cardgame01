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


import random
import time
from browser import document

#global

suits = ('rock', 'paper', 'scissors')
ranks = ('one', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
values = {'one':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'   # gives back Rock of three

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'the deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.point = 15

    def __repr__(self):
        return str(self)

    def add_card(self, card, index = 0):
        if index == 0:
            self.cards.append(card)
        else:
            self.cards.insert(index, card)


    def choose_card(self, index): # it returns the list of chosen card, ['paper', 6]
        chosen_card = self.cards.pop(index)
        card_info = (chosen_card.suit, values[chosen_card.rank])
        self.cards.insert(index, deck.deal())
        return card_info

    def damage(self, point):
        self.point -= point



def compare(player_card, pc_card):
    if player_card[0] == pc_card[0]:
        pass

    else:
        if player_card[0] == 'paper':
            if pc_card[0] == 'rock':
                pc_hand.damage(player_card[1])# put the def to work
                return('you win')
            else:
                player_hand.damage(pc_card[1])
                return('pc win')

        elif player_card[0] == 'scissors':
            if pc_card[0] == 'paper':
                pc_hand.damage(player_card[1])# put the def to work
                return('you win')
            else:
                player_hand.damage(pc_card[1])
                return('pc win')

        elif player_card[0] == 'rock':
            if pc_card[0] == 'scissors':
                pc_hand.damage(player_card[1])# put the def to work
                return('you win')
            else:
                player_hand.damage(pc_card[1])
                return('pc win')


def first_deal(player_hand, pc_hand):
    for hand in [player_hand, pc_hand]:
        for i in range(3):
            hand.add_card(deck.deal())

def show_card(player_hand, pc_hand):
    player = f'*{player_hand[0]} * {player_hand[1]} * {player_hand[2]} *'
    pc = f'*{pc_hand[0]} * {pc_hand[1]} * {pc_hand[2]} *'
    print('*' * len(player))
    print(player)
    print('*' * len(player))
    print('*' * len(pc))
    print(pc)
    print('*' * len(pc))

def show_battle(player_card, pc_card):
    print(f'your card: {player_card}, pc card: {pc_card}')


def show_point(player_hand, pc_hand):
    print(f'your point is {player_hand.point}')
    print(f'pc point is {pc_hand.point}')

def loser_judge(player_hand, pc_hand):
    if player_hand.point <= 0:
        return 0

    elif pc_hand.point <= 0:
        return 1

    else:
        pass

########################execution###################

deck = Deck()
deck.shuffle()
player_hand = Hand()
pc_hand = Hand()
first_deal(player_hand, pc_hand)


def main():
    global deck
    global player_hand
    global pc_hand
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    pc_hand = Hand()
    first_deal(player_hand, pc_hand)

main()

'''
while True:
    show_card(player_hand.cards, pc_hand.cards)


    player_card = player_hand.choose_card(int(input('input the card number: ')))
    pc_card = pc_hand.choose_card(random.randrange(0,3))

    show_battle(player_card, pc_card)

    compare(player_card, pc_card)
    show_point(player_hand, pc_hand)

    loser_judge(player_hand, pc_hand)
'''







