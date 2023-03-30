
from random import shuffle
from typing import Optional
from typing import Tuple
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
        """
        players: list of players
        deck: deck of cards
        dealAmount: amount of cards to deal to each player
        """
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

            dealer = self.players[self.round % len(self.players)]
            dealerIdx = self.players.index(dealer)
            print("Dealer: " + str(dealer.name))

            #players bid 
            
            highestbid, highestBidder = self.getHighestBidder(dealerIdx=dealerIdx)
            
            if highestBidder is not None:
                print("Highest Bidder: " + highestBidder.name)
                print(highestBidder.name + " bids " + str(highestbid))
            else:
                print("No bids, redeal")
                self.round += 1
            
            #select trump
            print(highestBidder.name + " Select trump")
            trump = input()
            if trump not in SUITS:
                raise Exception("Invalid suit")
            
            
            highestBidderIndex = self.players.index(highestBidder)
            self.passOrPlay(highestBidderIndex)
                    
                
            
            if (len(self.playing) == 1):
                # give 5 points to player
                continue

            for card in dealer.hand:
                for i in range(len(self.playing)):
                    player = self.players[(dealerIdx + i + 1 ) % len(self.players)]
                    for card in player.hand:
                        card.show()
                    print(player.name + " Select card index")
                    #follow suit and shit

                    cardIndex = int(input())
                    if cardIndex < 0 or cardIndex > len(self.players[dealerIdx].hand):
                        raise Exception("Invalid card index")
                # decide winner of trick
                # winner of hand must play first card next
                # 
            
            

            
            card = self.players[dealerIdx].hand.pop(cardIndex)
            highestBidder.score += 1
            self.round += 1

            #loop through players starting with left of dealer
            #player bid
            

        
            #player play card

            #player score trick


            #players play cards
            #players score tricks
    def getHighestBidder(self, dealerIdx: int) -> Tuple[int, Optional[Player]]:
        #loop through players starting with left of dealer
        highestBid = 0
        highestBidder = None
        for i in range(len(self.players)):
            player = self.players[(dealerIdx + i + 1 ) % len(self.players)]
            print(player.name + " bid")
            bid = int(input())
            if bid < 0 or bid > 5:
                raise Exception("Invalid bid")
            if(bid > highestBid):
                highestBid = bid
                highestBidder = player
            if(highestBid == 5):
                highestBid = bid
                highestBidder = player
                break
        return highestBid, highestBidder


    def passOrPlay(self, highestBidderIndex):
        for i in range(len(self.players) -1 ):
            player = self.players[(highestBidderIndex + i + 1 ) % len(self.players)]
            print(player.name + " pass or play")
            passOrPlay = input()
            if passOrPlay == "pass":
                continue
            elif passOrPlay == "play":
                self.playing
                self.playing.append(player)

    
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

    
