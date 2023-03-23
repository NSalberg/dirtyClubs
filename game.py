
from random import shuffle
from typing import Optional
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
    


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.score: int = 0
        

class Game:
    def __init__(self, players: list[Player], deck: Deck = Deck(), dealAmount: int = 0) -> None:
        self.players = players
        self.deck = deck
        self.round = 0
        self.dealAmount = dealAmount
        self.suit = ""
        self.playing: list[Player] = []

        if dealAmount * len(players) > len(deck.cards):
            raise Exception("Not enough cards in deck")
        
    def play(self) -> None:
        while self.hasPlayerWon:
            
            self.deal()
            
            self.showPlayersCards()

            dealer = self.round % len(self.players)
            print("Dealer: " + str(dealer))

            #players bid 
            #loop through players starting with left of dealer
            highestBid = 0
            highestBidder: Optional[Player] = None
            for i in range(len(self.players)):
                player = self.players[(dealer + i + 1 ) % len(self.players)]
                print(player.name + " bid")
                bid = int(input())
                if bid < 0 or bid > 5:
                    raise Exception("Invalid bid")
                if(bid > highestBid):
                    highestBid = bid
                    highestBidder = player
                if(highestBid == 5):
                    break
            if highestBidder is not None:
                print("Highest Bidder: " + highestBidder.name)
            else:
                print("No bids, redeal")
                self.round += 1
                break
            #select trump
            print(highestBidder.name + " Select trump")
            trump = input()
            if trump not in SUITS:
                raise Exception("Invalid suit")
            
            
            #loop through players starting with left of highest bidder
            highestBidderIndex = players.index(highestBidder)

            for i in range(len(self.players) -1 ):
                player = self.players[(highestBidderIndex + i + 1 ) % len(self.players)]
                print(player.name + " pass or play")
                passOrPlay = input()
                if passOrPlay == "pass":
                    continue
                elif passOrPlay == "play":
                    self.playing
                    self.playing.append(player)
                    
                
            #dealer play card
            print(self.players[dealer].name + " Select card")
            cardIndex = int(input())
            if cardIndex < 0 or cardIndex > len(self.players[dealer].hand):
                raise Exception("Invalid card index")
            card = self.players[dealer].hand.pop(cardIndex)
            highestBidder.score += 1
            self.round += 1
            #loop through players starting with left of dealer
            #player bid
            

        
            #player play card

            #player score trick


            #players play cards
            #players score tricks
    
    def hasPlayerWon(self) -> bool:
        for player in self.players:
            if player.score >= 15:
                return True
        return False
    
    def deal(self) -> None:
        for player in self.players:
            for _ in range(self.dealAmount):
                player.hand.append(self.deck.draw())
    def showPlayersCards(self) -> None:
        for player in self.players:
            print(player.name)
            for card in player.hand:
                card.show()
            print("")

if __name__ == "__main__":
    deck = Deck([1,9,10,11,12,13])
    players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]
    game = Game(players, deck, 5)
    game.play()

    