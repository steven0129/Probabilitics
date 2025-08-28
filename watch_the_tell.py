import random
import math


class CardGame:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['H', 'D', 'C', 'S']

    def __init__(self, rng=None):
        self.rng = rng if rng is not None else random.Random()

    def build_deck(self):
        return [f"{rank}{suit}" for suit in self.SUITS for rank in self.RANKS]

    def deal_cards(self):
        deck = self.build_deck()
        self.rng.shuffle(deck)
        seen = deck[:7]
        opponent = deck[7:9]
        return seen, opponent

    def format_cards(self, cards):
        return ', '.join(cards)

    def compute_win_probabilities(self, seen, tell):
        remaining_cards = 52 - len(seen)
        aces_seen = sum(1 for c in seen if c.startswith('A'))
        aces_remaining = 4 - aces_seen
        total_pairs = math.comb(remaining_cards, 2)
        no_ace_pairs = math.comb(remaining_cards - aces_remaining, 2)
        p_win_prior = 0.0 if total_pairs == 0 else no_ace_pairs / total_pairs
        p_H = 1 - p_win_prior
        if tell:
            denom = 0.5 * p_H + 0.1 * (1 - p_H)
            p_H_post = 0.0 if denom == 0 else (0.5 * p_H) / denom
        else:
            denom = 0.5 * p_H + 0.9 * (1 - p_H)
            p_H_post = 0.0 if denom == 0 else (0.5 * p_H) / denom
        p_win_post = 1 - p_H_post
        return p_win_prior, p_win_post

    def get_yes_no(self, prompt):
        while True:
            choice = input(prompt).strip().lower()
            if choice in ('y', 'yes'):
                return True
            if choice in ('n', 'no'):
                return False
            print("Please type 'y' or 'n'.")


if __name__ == "__main__":
    game = CardGame()
    print("You are playing a game. Your opponent has 2 unseen cards. If either is an ace, you lose ...")
    seen, opponent = game.deal_cards()
    has_winning_hand = any(card.startswith('A') for card in opponent)
    tell = game.rng.random() < (0.5 if has_winning_hand else 0.1)

    print("The following cards are seen by you:")
    print(game.format_cards(seen))
    print("")

    print("Opponent shows an excited tell!" if tell else "Opponent does NOT show an excited tell...")

    # Calculate and display your win probability before deciding to play
    p_win_prior, p_win_post = game.compute_win_probabilities(seen, tell)
    print(f"Your win probability (ignoring the tell): {p_win_prior*100:.2f}%")
    print(f"Your win probability (after observing the tell): {p_win_post*100:.2f}%")

    play = game.get_yes_no("Do you choose to play? (y/n): ")
    if play:
        print("")
        if has_winning_hand:
            print("You lose!!!")
        else:
            print("You win!!!")

    print("")
    print("Opponent's cards were:")
    print(game.format_cards(opponent))