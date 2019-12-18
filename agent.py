import random
from probs import *

dice_faces = range(1, 6 + 1)

def index(bid):
    return ranked_bids.index(bid)

def available_bids(current_bid, n_higher_bids):
    quantity, value = current_bid
    current_bid_index = index(current_bid)
    bids = []
    for i in range(1, n_higher_bids + 1):
        bid_index = current_bid_index + i
        bids.append(ranked_bids[bid_index])
    return bids

class Agent:
    def __init__(self, n_starting_dice=5, c=0.5):
        self.c = c
        self.dice_faces = dice_faces
        self.n_current_dice = n_starting_dice
        self.roll_dice()
        self.ranked_bids = []
        for q in range(1, total_dice + 1):
            for v in dice_faces:
                self.ranked_bids.append((q, v))

    def is_out(self):
        return self.n_current_dice < 1

    def roll_dice(self):
        self.dice = random.choices(self.dice_faces, k=self.n_current_dice)

    def lose_dice(self):
        self.n_current_dice -= 1

    def n_of_value(self, value):
        return len([d for d in self.dice if d == value])

    def react(self, current_bid, ranked_bids, total_dice):
        bids = available_bids(current_bid, 10)
        bid_probs = [(bid, prob_bid(bid, self.dice, total_dice)) for bid in bids]
        acceptable_bids = [(b, p) for (b, p) in bid_probs if p > self.c]

        print(acceptable_bids)

        if acceptable_bids == []:
            return 'perudo'
        best_bid, _ = min(acceptable_bids, key=lambda a: a[1])
        return best_bid
