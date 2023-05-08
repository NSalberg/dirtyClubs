from random import shuffle
SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
class Card:
    def __init__(self, suit: str, number: int) -> None:
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


if __name__ == "__main__":
    deck = Deck([1,9,10,11,12,13])
    deck.show()