def generate_ranked_bids(min_dice, total_dice, dice_faces):
    ranked_bids = []
    for q in range(min_dice, total_dice + 1):
        for v in dice_faces:
            ranked_bids.append((q, v))
    return ranked_bids
