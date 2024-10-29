import random

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def main():
    deck = create_deck()

    try:
        num_players = int(input("Enter the number of players (2-5): "))
        if num_players < 2 or num_players > 5:
            print("Error: Number of players must be between 2 and 5!")
            return
    except ValueError:
        print("Error: Invalid input for number of players!")
        return

    cards_per_player = []
    total_cards_needed = 0

    for i in range(num_players):
        try:
            num_cards = int(input(f"Enter the number of cards for Player {i + 1}: "))
            cards_per_player.append(num_cards)
            total_cards_needed += num_cards
        except ValueError:
            print("Error: Invalid input for number of cards!")
            return

    if total_cards_needed > len(deck):
        print("Error: Not enough cards in the deck!")
        return

    for i in range(num_players):
        print(f"\nPlayer {i + 1}'s hand:")
        hand = deck[:cards_per_player[i]]
        deck = deck[cards_per_player[i]:]
        for rank, suit in hand:
            print(f"{rank} of {suit}")

    print("Hands dealt successfully!")


if __name__ == "__main__":
    main()