from Game import *






players = {'Omry': 100, 'Evan': 100}


'''
    def fold(self):
        self.hand = []

    def evaluate_hand(self):
        hand_ranks = [card.rank for card in self.hand]
        if all(rank in hand_ranks for rank in ['10', 'J', 'Q', 'K', 'A']) and \
                all(card.suit == self.hand[0].suit for card in self.hand):
            return "Royal flush"
        elif all(card.suit == self.hand[0].suit for card in self.hand) and \
                all(int(rank) in range(2, 10) for rank in hand_ranks):
            return "Straight flush"
        elif all(rank == self.hand[0].rank for rank in hand_ranks):
            return "Four of a kind"
        elif sorted(hand_ranks) == ['2', '3', '4', '5', 'A'] and \
                all(card.suit == self.hand[0].suit for card in self.hand):
            return "Straight flush with A-5 low"
        elif all(card.suit == self.hand[0].suit for card in self.hand):
            return "Flush"
        elif sorted(hand_ranks) == ['A', '2', '3', '4', '5']:
            return "Straight with A-5 low"
        elif len(set(hand_ranks)) == 2:
            return "Full house"
        elif len(set(hand_ranks)) == 3 and any(hand_ranks.count(rank) == 3 for rank in hand_ranks):
            return "Three of a kind"
        elif sorted(hand_ranks) == ['10', 'J', 'Q', 'K', 'A']:
            return "Straight with 10-A high"
        elif len(set(hand_ranks)) == 4:
            return "Two pairs"
        elif len(set(hand_ranks)) == 3:
            return "One pair"
        else:
            return "High card"
'''