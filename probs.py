import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def prob_exactly(n, r, matching_dice):
    p = len(matching_dice)/6
    return ncr(n, r) * pow(p, r) * pow(1 - p, n - r)

def prob_bid(bid, dice, total_dice, palafico=False):
    quantity, value = bid
    unknown_dice = total_dice - len(dice)

    matching_dice = [value]
    if not palafico:
        matching_dice.append(1)
    residual_quantity = max(0, quantity - len([d for d in dice if d in matching_dice]))
    # What is the probability of the unknown dice having at least residual_quantity of value?

    prob = 1 - sum(prob_exactly(unknown_dice, i, matching_dice) for i in range(residual_quantity))
    return prob

print(prob_bid((4, 5), [1, 3, 2, 5, 5], 15, False))
