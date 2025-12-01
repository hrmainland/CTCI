from dataclasses import dataclass
from typing import List
from itertools import product
from random import shuffle
from enum import Enum


class Suit(Enum):
    SPADE = "spade"
    CLUB = "club"
    DIAMOND = "diamond"
    HEART = "heart"


class Deck:
    def __init__(self, card_type, hand_type):
        suits = [Suit.SPADE, Suit.CLUB, Suit.DIAMOND, Suit.HEART]
        ranks = [num for num in range(1, 14)]
        self.available = [card_type(rank, suit) for rank, suit in product(ranks, suits)]
        self.dealt = set()
        self.hand_type = hand_type

    def shuffle(self):
        shuffle(self.available)

    def deal(self, num_cards, num_hands):
        if num_cards * num_hands > len(self.available):
            raise Exception(
                f"{len(self.available)} cards cannot be dealt between {num_hands} players with {num_cards} each"
            )
        card_lists = [[] for _ in range(num_hands)]
        for _ in range(num_cards):
            for i in range(num_hands):
                card = self.available.pop()
                card_lists[i].append(card)
                self.dealt.add(card)
        return [self.hand_type(cards) for cards in card_lists]


@dataclass(frozen=True)
class Card:
    def __init__(self, rank: int, suit: Suit):
        self.rank = rank
        self.suit = suit
        self.face_value = (
            rank if 1 < rank < 11 else {1: "A", 11: "J", 12: "Q", 13: "K"}[rank]
        )


class BlackJackCard(Card):
    def __init__(self, rank: int, suit: Suit):
        super().__init__(rank, suit)
        self.scores = [rank] if rank != 1 else [1, 11]


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards


class BlackJackHand(Hand):
    def __init__(self, cards: List[Card]):
        super().__init__(cards)
        self.score = self.get_score()

    def get_score(self):
        combos = list(product(*[card.scores for card in self.cards]))
        sums = [sum(combo) for combo in combos]
        unders = [elem for elem in sums if elem <= 21]
        return max(unders) if unders else min(sums)


# d3 = Card(3, Suit.DIAMOND)
da = BlackJackCard(1, Suit.DIAMOND)
d2 = BlackJackCard(2, Suit.DIAMOND)
d10 = BlackJackCard(10, Suit.DIAMOND)
hand = BlackJackHand([d10, da, da, d2, d10])
print(hand.score)

deck = Deck(BlackJackCard, BlackJackHand)
deck.shuffle()
hands = deck.deal(5, 4)
print(hands[0].score)
