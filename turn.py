from cards import Card, Deck
from players import Player
class Turn:
    def __init__(self, deck:Deck , players: list[Player], agent, dealAmount: int = 0):
        """"
        deck: deck of cards
        players: list of players
        agent: agent
        dealAmount: amount of cards to deal to each player"""
        self.deck = deck
        self.players = players
        self.agent = agent
        self.dealAmount = 4
        if dealAmount * len(players) > len(deck.cards):
            raise Exception("Not enough cards in deck")
        self.deal()

    

    def deal(self) -> None:
        for player in self.players:
            for _ in range(self.dealAmount):
                player.hand.append(self.deck.draw())
        
