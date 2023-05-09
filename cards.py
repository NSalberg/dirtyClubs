from random import shuffle
from enum import Enum

class Suit(Enum):
    HEARTS = 1
    SPADES = 2
    CLUBS = 3
    DIAMONDS = 4
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Suit):
            return self.value == other.value
        return False
    def __hash__(self) -> int:
        return self.value
    def __str__(self) -> str:
        return self.name.lower()
class Card:
    def __init__(self, suit: Suit, number: int) -> None:
        self.suit = suit
        self.number = number

    def __eq__(self, card: object) -> bool:
        if isinstance(card, Card):
            return self.number == card.number and self.suit == card.suit
        return False
    
    def __str__(self) -> str:
        if self.number == 1:
            num = "Ace"
        elif self.number == 11:
            num = "Jack"
        elif self.number == 12:
            num = "Queen"
        elif self.number == 13:
            num = "King"
        else:
            num = str(self.number)
        return "{} of {}".format(num, self.suit)
    def show(self) -> None:
        print(self)
    

class Deck:
    def __init__(self, range: list[int] = list(range(1,14)) ) -> None:
        self.cards = list[Card]()
        self.range = range
        self.build(range = range)
        self.shuffle()

    def build(self, range: list[int]):
        for n in range:
            for s in Suit:
                self.cards.append(Card(s,n))
    
    def draw(self) -> Card:
        return self.cards.pop()
    
    def show(self) -> None:
        for card in self.cards:
            card.show()

    def shuffle(self) -> None:
        shuffle(self.cards)


if __name__ == "__main__":
    deck = Deck([1,9,10,11,12,13])
    deck.show()