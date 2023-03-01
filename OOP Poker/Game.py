from Player import *
from Deck import *

class PokerGame:
    def __init__(self, players):
        self.players = [Player(name, chips) for name, chips in players.items()]
        self.deck = Deck()
        self.pot = 0
        self.round = 0
        self.canCheck = True
        self.maxBet = 0
        self.sidePot = 0
        self.isSidePot = False

    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                card = self.deck.draw_card()
                player.receive_card(card)

    def show_hands(self):
        for player in self.players:
            print(f"{player.name} has: {' | '.join(player.show_hand())}")

    def bet(self, player):
        bet_amount = int(input(f"{player.name}, how much would you like to bet? "))
        while player < bet_amount or bet_amount < self.maxBet:
            if player.chips < bet_amount:
                print("Player doesn't have enough chips to bet that amount.")
                bet_amount = int(input(f"{player.name}, how much would you like to bet? "))
            elif bet_amount < self.maxBet:
                print(f"The player before you has bet {self.maxBet}. You must match his bet or bet more in order to continue playing.")
                bet_amount = int(input(f"{player.name}, how much would you like to bet? "))

        player.chips -= bet_amount
        if self.sidePot:
            self.sidePot += bet_amount
        else:
            self.pot += bet_amount

    def call(self, player):

        if player.chips <= self.maxBet:
            self.sidePot = True
            self.allIn(player)
        else:
            self.pot += self.maxBet
            player.chips -= self.maxBet


    def allIn(self, player):
        if self.sidePot:
            self.sidePot += player.chips
            player.chips -= player.chips
        else:
            self.pot += player.chips
            player.chips -= player.chips


    def gameOptions(self, player, canCheck):
        if canCheck:
            choice = int(input(f'(0): Fold. (1): Check. (2): Bet. (3): All in.'))
            if choice == 0:
                player.fold()
                self.players.remove(player)
                return 0
            elif choice == 1:
                print(f'{player.name} checks.')
                return 0
            elif choice == 2:
                betAmount = self.bet(player)
                return betAmount
            elif choice == 3:
                pass
        else:
            choice = int(input(f'(0): Fold. (1): Call. (2): Bet. (3): All in.'))
            if choice == 0:
                player.fold()
                self.players.remove(player)
                return 0
            elif choice == 1: # Fix
                pass


    def play_round(self):
        if self.round == 0:
            self.maxBet = 0
            self.deal_cards()
            self.show_hands()
            for player in self.players:
                if player.chips > 0:
                    choice = self.gameOptions(player, self.canCheck)
                    self.maxBet = max(choice, self.maxBet)
                else:
                    continue

    def play_game(self):
        while True:
            self.play_round()