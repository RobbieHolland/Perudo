from probs import *
from ranked_bids import *
from agent import Agent

n_agents = 6
n_dice = 5
total_dice = 24
agents = []

for i in range(n_agents):
    agents.append(Agent(n_starting_dice=n_dice))

def bid_checks(bid, agents):
    quantity, value = bid
    n_with_value = sum([a.n_with_value(value) for a in agents])
    return n_with_value >= quantity

def alive(agents):
    return [a for a in agents if not a.is_out()]

def play_game(agents):
    current_agent = 0
    prev_a = None
    n_dice_total = sum([a.n_current_dice for a in agents])
    current_bid = (1, 1)

    while len(alive(agents)) > 1:
        agent = agents[current_agent % len(alive(agents))]
        if agent.is_out():
            current_agent = (current_agent + 1) % n_agents
            continue

        n_dice_total = sum([a.n_current_dice for a in agents])
        action = agent.react(current_bid, ranked_bids, n_dice_total)

        if action == 'perudo':
            if bid_checks(bid, agents):
                a.lose_dice()
            else:
                prev_a.lose_dice()
            [a.roll_dice() for a in agents]
            current_bid = (1, 1)
            n_dice_total -= 1
        else:
            current_bid = action
        prev_a = agent
    return alive(agents)[0]

ranked_bids = generate_ranked_bids(total_dice)

print(play_game(agents))
