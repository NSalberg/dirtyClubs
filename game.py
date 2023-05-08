from turn import Turn
from typing import Optional
from typing import Tuple
from cards import Deck, SUITS, Card
from players import Player
from utils import block_print
import copy

class ClubsEngine:
    def __init__(self, num_players: int, deck: Deck = Deck(), dealAmount: int = 0, comment : bool = False) -> None:
        """
        players: list of players
        deck: deck of cards
        dealAmount: amount of cards to deal to each player
        """
        self.players = list[Player]()
        self.num_players = num_players
        self.full_deck = deck
        self.deck = Deck()
        self.dealAmount = dealAmount
        """
        self.turn = Turn(
            deck=self.deck,
            players=self.players,
            agent=None,
            dealAmount = self.dealAmount
        )
        """
        self.player_scores = [0,0,0,0]
        self.round = 0
        self.trump = ""
        self.playing: list[Player] = []
    
        if comment == False: block_print()
        
        
    def play(self) -> list[int]:
        while self.hasPlayerWon():
            self.deck = copy.deepcopy(self.full_deck)
            self.deal()
            start_player = self.players[0]
            while self.players[0].hand != []:
                start_player = self.trick(start_player)
            print(self.player_scores)
            self.round += 1
            
        return self.player_scores
            

    # TODO: implement trump suit 
    def trick(self, starting_player: Player) -> Player:
        print(f"Trick starting with : {starting_player.name}")
        starting_player_idx = self.players.index(starting_player)
        cards_played = list[Tuple[Player,Card]]()

        for i in range(len(self.players)):
            player = self.players[(starting_player_idx + i) % len(self.players)]
            card_played = player.play_random(lead_card=None)
            print(f"{player.name} played {card_played}")
            cards_played.append((player, card_played))
            # is not removing card from hand
            # notify all agents of a move 
            for notified_player in self.players:
                notified_player.observeActionTaken(player, card_played)
        # find winner of trick
        winner = self.find_winner(cards_played)
        print(f"Winner of trick: {winner.name}\n")
        self.player_scores[self.players.index(winner)] += 1
        return winner

    def find_winner(self, cards_played: list[Tuple[Player,Card]]) -> Player:
        # find highest card of lead suit or trump
        
        highest_card = cards_played[0][1]
        lead = highest_card.suit
        winner = cards_played[0][0]
        for player, card in cards_played:
            if card.suit == lead:
                if card.number > highest_card.number:
                    highest_card = card
                    winner = player
        return winner

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
        #check if any player has 15 points or more
        if any(score >= 15 for score in self.player_scores):
            return False
        return True
    
    def deal(self) -> None:
        self.deck.shuffle()
        self.players = []
        for i in range(num_players):
            hand = []
            for _ in range(self.dealAmount):
                hand.append(self.deck.draw())
            self.players.append(Player("Player " + str(i+1), hand))
        self.showPlayersCards()

    def showPlayersCards(self) -> None:
        for player in self.players:
            print(player.name)
            for card in player.hand:
                card.show()
            print("")

if __name__ == "__main__":
    deck = Deck([1,9,10,11,12,13])
    num_players = 4
    game = ClubsEngine(num_players, deck, 5, True)
    game.play()

    
