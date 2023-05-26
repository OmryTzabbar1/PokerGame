from Player import *
from Deck import *
from collections import Counter



class PokerGame:
    bigBlindPos = -1
    def __init__(self, players):
        self.players = [Player(name, chips) for name, chips in players.items()]
        self.deck = Deck()
        self.pot = 0
        self.minBet = 0
        self.round = 0
        self.canCheck = True
        self.sidePot = 0
        self.isSidePot = False
        self.bigBlind = 2
        self.straddleNum = 0
        self.board = []
        PokerGame.bigBlindPos += 1
        PokerGame.bigBlindPos % len(players)

    def straddle(self):
        self.straddleNum += 1

    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                card = self.deck.draw_card()
                player.receive_card(card)

    def bet(self, player):

        bet_amount = self.minBet

        allIn, threeQuart, halfPot, quartPot, tenCent, minBet = self.minBet, self.pot * (3/4), self.pot / 2, \
                                            self.pot / 4, self.pot / 10, self.bigBlind * (self.straddleNum + 1)

        print(f"Total: {bet_amount} ({bet_amount/player.chips})% of your stack.")
        tempAmount = int(input(f"{player.name}, how much would you like to bet?"
                                   f"(1 = All in) "
                                   f"(2 = 75% pot)"
                                   f"(3 = 50% pot)"
                                   f"(4 = 25% pot)"
                                   f"(5 = 10% pot)"
                                   f"(6 = {minBet})"))

        if tempAmount == 1:
            self.allIn(player)
        elif tempAmount == 2:
            bet_amount = self.pot*.75
        elif bet_amount == 3:
            bet_amount = self.pot/4.0
        elif bet_amount == 4:
            bet_amount = self.pot/4.0
        elif bet_amount == 5:
            bet_amount = self.pot/10
        elif bet_amount == 6:
            bet_amount = self.minBet

        player.bet(bet_amount)
        if self.sidePot:
            self.sidePot += bet_amount
        else:
            self.pot += bet_amount
            self.minBet = bet_amount

    def call(self, player):

        if player.chips <= self.minBet:
            self.sidePot = True
            self.allIn(player)
        else:
            if self.sidePot:
                self.sidePot += self.minBet
                player.bet(self.minBet)
            else:
                self.pot += self.minBet
                player.bet(self.minBet)

    def allIn(self, player):
        if self.sidePot:
            self.sidePot += player.chips
            player.bet(player.chips)
        else:
            self.pot += player.chips
            player.bet(player.chips)

    def gameOptions(self, player, canCheck):
        if canCheck:
            choice = int(input(f'(0): Fold. (1): Check. (2): Bet. (3): All in.'))
            if choice == 0: # Enum
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

    def checkForStreight(self, list):
        count = 1

        for i in range(len(list)):

            if count == 5:
                return True

            try:
                if list[i] == list[i + 1] - 1:
                    count += 1
                else:
                    count = 1
            except:
                return False

    def evaluate_hand(self, hand):
        ranks = [card.getRank() for card in hand]
        suits = [card.getSuit() for card in hand]

        # check for flush
        if 5 in Counter(suits).values():
            if self.checkForStreight(ranks):
                return '9'
            else:
                return '8'

        # check for straight
        elif self.checkForStreight(ranks):
            return '7'

        # check for four of a kind
        elif 4 in Counter(ranks).values():
            return '6'

        # check for full house
        elif 2 in Counter(ranks).values() and 3 in Counter(ranks).values():
            return '5'

        # check for three of a kind
        elif 3 in Counter(ranks).values():
            return '4'

        # check for two pair
        elif list(Counter(ranks).values()).count(2) == 2:
            return '3'

        # check for one pair
        elif 2 in Counter(ranks).values():
            return '2'

        # otherwise, the hand must be high card

        else: return '1'



    def show_hands(self):
        for player in self.players:
            print(f"{player.name} has: {' | '.join(player.show_hand())}")

    def play_round(self):
        if self.round == 0:
            self.bet_amount = 0
            self.deal_cards()
            self.show_hands()
            for player in self.players:
                if player.chips > 0:
                    choice = self.gameOptions(player, self.canCheck)
                    self.bet_amount = max(choice, self.bet_amount)
                else:
                    continue
            self.minBet = 0
            self.round += 1

    def play_game(self):
        while True:
            self.play_round()

