from typing import Optional, Union, Tuple, Type
from cards import Deck, Suit, Card
from players import Player, Player_Random
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
            dealerIdx = self.round % len(self.players)
            start_player = self.players[dealerIdx]
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
            #change lead card to first card played
            if i == 0:
                card_played = player.play_card(lead_card=None)
                self.lead_card = card_played
            else:
                card_played = player.play_card(lead_card=self.lead_card)
            
            print(f"{player.name} played {card_played}")
            cards_played.append((player, card_played))

            # notify all agents of a move 
            for notified_player in self.players:
                notified_player.observeActionTaken(player, card_played)
        # find winner of trick
        winner = self.find_winner(cards_played, trump=self.trump)
        print(f"Winner of trick: {winner.name}\n")
        self.player_scores[self.players.index(winner)] += 1
        return winner

    # TODO: this function sucks make it better, less confusing, and more efficient
    def find_winner(self, cards_played: list[Card], trump: Optional[Suit]) -> int:
        """
        find_winner finds the winner of a trick and returns the index of the winner
        :param cards_played: list of cards played in the trick
        :param trump: trump suit
        :return: index of the winner
        """
        card_values = [card.number for card in cards_played]
        cards_hierarchy = list[Card]()
        opposite_color_suit = Suit
        if trump is not None:
            cards_hierarchy = self.generateTrumpHierarchy(trump)
            opposite_color_suit = trump.opposite_suit_same_color()


        highest_card = cards_played[0]
        lead_suit = cards_played[0].suit
        
        if trump is not None:
            for card in cards_played:
                if card.suit == trump or (card.suit == opposite_color_suit and card.number == 11):
                    if highest_card.suit != trump and (highest_card.suit != opposite_color_suit and highest_card.number != 11):
                        highest_card = card
                    elif cards_hierarchy.index(card) < cards_hierarchy.index(highest_card):
                        highest_card = card
                elif card.suit == lead_suit and (highest_card.suit != trump and (highest_card.suit != opposite_color_suit and highest_card.number != 11) ):
                    if card.number > highest_card.number:
                        highest_card = card
        return cards_played.index(highest_card)
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

    # generate card hierarchy
    def generateTrumpHierarchy(self,  trump: Suit) -> list[Card]:
        hierarchy = list[Card]()
        hierarchy.append(Card(trump, 11))
        hierarchy.append(Card(trump.opposite_suit_same_color(), 11))
        hierarchy.append(Card(trump, 14))
        hierarchy.append(Card(trump, 13))
        hierarchy.append(Card(trump, 12))
        hierarchy.append(Card(trump, 10))
        hierarchy.append(Card(trump, 9))
        return hierarchy
    """
    def generateHierarchy(self, deck: Deck, lead: Suit, isTrump: bool) -> list[Card]:
        deck = copy.deepcopy(deck)
        for card in deck.cards:
            if card.suit == lead:
                card.number += 13
    """

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
            self.players.append(Player_Random("Player " + str(i+1), hand))
        #self.showPlayersCards()

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

    
