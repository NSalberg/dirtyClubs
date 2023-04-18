from typing import Optional
from random import shuffle
SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
class Card:
    def __init__(self, suit: str, number: int) -> None:
        self.suit = suit
        self.number = number

    def show(self) -> None:
        print("{} of {}".format(self.number, self.suit))

class Deck:
    def __init__(self, range: list[int] = list(range(1,14)) ) -> None:
        self.cards = []
        self.range = range
        self.build(range = range)
        self.shuffle()


        
    def build(self, range: list[int]):
        for n in range:
            for s in SUITS:
                self.cards.append(Card(s,n))
    
    def draw(self) -> Card:
        return self.cards.pop()
    
    def show(self) -> None:
        for card in self.cards:
            card.show()

    def shuffle(self) -> None:
        shuffle(self.cards)