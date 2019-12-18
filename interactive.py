from probs import *
from ranked_bids import *

print('How many dice total?')
total_dice = int(input())

dice_faces = range(1, 6 + 1)
min_dice, max_dice = 1, 10
ranked_bids = generate_ranked_bids(min_dice, max_dice, dice_faces)

while True:
    print('There are', total_dice, 'total dice. What are your dice?')
    dice = [int(d) for d in input().split(' ')]
    print('Palafico?')
    answer = input()
    palafico = 'y' in answer

    bid_probs = [(bid, prob_bid(bid, dice, total_dice, palafico)) for bid in ranked_bids]
    bid_probs = sorted(bid_probs, key=lambda bp: bp[1], reverse=True)
    bid_probs = list(filter(lambda bp: bp[1] > 0.3 and bp[1] < 1, bid_probs))
    for bid, prob in bid_probs:
        print(bid, '=', round(100 * prob, 2), '%')

    total_dice -= 1
