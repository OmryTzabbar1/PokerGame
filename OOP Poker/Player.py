class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.chipsIn = 0

    def receive_card(self, card):
        self.hand.append(card)

    def evaluateHand(self, board):
        pass

    def show_hand(self):
        return [str(card) for card in self.hand]

    def fold(self):
        self.hand = []

    def bet(self, chips):
        self.chipsIn += chips
        self.chips -= chips