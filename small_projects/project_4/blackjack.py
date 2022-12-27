"""Blackjack, by Hideaki Fukami
The classic card game also known as 21."""

import random, sys

# Set up the constants:
HEARTS = chr(9829) # '♥'
DIAMONDS = chr(9830) # '♦'
SPADES = chr(9824) # '♠'
CLUBS = chr(9827) # '♣'
BACKSIDE = 'backside'

def main():
    print('''Blackjack, by Hideaki Fukami
    
    Rules:
        Try to get as closse to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exatly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')
    
    money = 5_000
    while True: # Main game loop.
        if money <= 0:
            print("You're broke!\nGood thing you weren't playing real money.\nThanks for playing!")
            sys.exit()
        
        # Enter the bet:
        print(f'Money: {money}')
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

def getBet(maxBet):
    while True: # Keep asking until they enter a valid amount.
        print(f'How much do you bet? (1-{maxBet}, or QUIT)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal():
            continue
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck