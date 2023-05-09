from collections import defaultdict
from cards import Card, Deck
from typing import Optional, List, Tuple
import random
from abc import abstractmethod, ABC

class Player(ABC):
    @abstractmethod
    def __init__(self, name: str, hand) -> None:
        self.name = name
        self.hand = hand
        self.hand_playable = list[Card]()
        self.score: int = 0
        self.in_play = list[Card]()
        self.card_map = defaultdict(list)
        for card in hand:
            self.card_map[card.suit].append(card)    
    
    """
    @param lead_card: card that was played first if it is the first card in the trick lead_card is None
    @return: card that was played
    """
    @abstractmethod
    def play_card(self, lead_card: Optional[Card]) -> Card:
        """
        play_card is called by the game engine to get the card that the player wants to play
        
        :param lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        self.find_playable(lead_card)
        played_card = random.choice(self.hand_playable)
        self.hand.remove(played_card)
        return played_card
    
    """
    @param player: player that played the card
    @param card: card that was played
    """
    @abstractmethod
    def observeActionTaken(self, player, card: Card) -> None:
        """
        observeActionTaken is called by the game engine to notify the player of a move
        
        :param player: player that played the card
        :param card: card that was played
        """
        if player == self:
            self.card_map[card.suit].remove(card)
        self.in_play.append(card) 

        #TODO: this should only happen when the trick is over change 4 to however many players there are
        if len(self.in_play) == 4:
            self.in_play.clear()
            self.lead_card = None
    
    
    def find_playable(self, lead_card: Optional[Card]) -> List[Card]:
        """
        find_playable looks at the players hand and finds playable cards, then adds them to hand_play
        
        :param lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        
        self.hand_playable = list[Card]()
        # add jack of opposite suit to playable

        #if lead_card is None or player does not have suit of lead_card add all cards to playable
        if lead_card is None or not self.has_suit(lead_card.suit):
            for card in self.hand:
                self.hand_playable.append(card)
        else:
            #if player has suit of lead_card add all cards of that suit to playable
            for card in self.hand:
                if  card.suit == lead_card.suit:
                    self.hand_playable.append(card)
                elif (lead_card.suit == "Hearts" or lead_card.suit == "Diamonds") and (card.number == 11 and (card.suit == "Hearts" or card.suit == "Diamonds")):
                    self.hand_playable.append(card)
                elif (lead_card.suit == "Clubs" or lead_card.suit == "Spades") and (card.number == 11 and (card.suit == "Clubs" or card.suit == "Spades")):
                    self.hand_playable.append(card)
        return self.hand_playable

    def has_suit(self, leadsuit: str) -> bool:
        for card in self.hand:
            if card.suit == leadsuit:
                return True
            if (leadsuit == "Hearts" or leadsuit == "Diamonds") and (card.number == 11 and (card.suit == "Hearts" or card.suit == "Diamonds")):
                return True
            if (leadsuit == "Spades" or leadsuit == "Clubs") and (card.number == 11 and (card.suit == "Clubs" or card.suit == "Spades")):
                return True
        return False

    def __eq__(self, player: object) -> bool:
        if isinstance(player, Player):
            return self.name == player.name
        return False


class Player_Random(Player):
    def __init__(self, name: str, hand) -> None:
        self.name = name
        self.hand = hand
        self.hand_playable = list[Card]()
        self.score: int = 0
        self.in_play = list[Card]()
        self.card_map = defaultdict(list)
        for card in hand:
            self.card_map[card.suit].append(card)    
    
    def play_card(self, lead_card: Optional[Card]) -> Card:
        """
        play_card plays a random card from the hand_playable
        
        lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        self.find_playable(lead_card)
        played_card = random.choice(self.hand_playable)
        self.hand.remove(played_card)
        return played_card
    
    def observeActionTaken(self, player, card: Card) -> None:
        if player == self:
            self.card_map[card.suit].remove(card)
        self.in_play.append(card) 

        #TODO: this should only happen when the trick is over change 4 to however many players there are
        if len(self.in_play) == 4:
            self.in_play.clear()
            self.lead_card = None
        
