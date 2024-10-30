import random
from collections import Counter

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def hand_rank(cards):
    values = sorted([card[0] for card in cards], key=VALUES.index)
    value_counts = Counter(values)
    pairs = sum(1 for count in value_counts.values() if count == 2)
    trips = sum(1 for count in value_counts.values() if count == 3)
    quads = sum(1 for count in value_counts.values() if count == 4)

    if quads:
        return (7, values)
    elif trips and pairs:
        return (6, values)
    elif trips:
        return (3, values)
    elif pairs == 2:
        return (2, values)
    elif pairs:
        return (1, values)
    else:
        return (0, values)

def simulate_poker(num_players=2):
    deck = [(value, suit) for suit in SUITS for value in VALUES]
    random.shuffle(deck)
    
    player_hands = {f"Player {i+1}": [deck.pop(), deck.pop()] for i in range(num_players)}
    community_cards = [deck.pop() for _ in range(5)]
    
    best_hands = {player: hand_rank(hand + community_cards) for player, hand in player_hands.items()}
    winner = max(best_hands, key=best_hands.get)

    print("Community Cards:", community_cards)
    for player, hand in player_hands.items():
        print(f"{player}'s Hand: {hand}")
    print("Winner:", winner)

num_players=int(input("Enter number of players: "))
simulate_poker(num_players)