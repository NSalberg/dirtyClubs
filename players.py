from collections import defaultdict
from cards import Card, Deck, Suit
from typing import Optional, List, Tuple
import random
from abc import abstractmethod, ABC

class Player(ABC):
    @abstractmethod
    def __init__(self, name: str, hand: list[Card]) -> None:
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
    def play_card(self, lead_card: Optional[Card], trump_suit: Suit) -> Card:
        """
        play_card is called by the game engine to get the card that the player wants to play
        
        :param lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        self.find_playable(lead_card, trump_suit)
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
    
    
    def find_playable(self, lead_card: Optional[Card], trump_suit: Suit) -> List[Card]:
        """
        find_playable looks at the players hand and finds playable cards, then adds them to hand_play
        
        :param lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        
        self.hand_playable = list[Card]()
        # add jack of opposite suit to playable
        if lead_card is None:
            for card in self.hand:
                self.hand_playable.append(card)
            return self.hand_playable
        
        #if lead card is a jack of opposite suit of trump lead suit is actually trump suit
        if lead_card.suit == trump_suit.opposite_suit_same_color() and lead_card.number == 11:
            lead_card.suit = trump_suit

        for card in self.hand:
            if card.suit == lead_card.suit and not (card.number == 11 and (card.suit == trump_suit or card.suit == trump_suit.opposite_suit_same_color())):
                self.hand_playable.append(card)
            elif lead_card.suit == trump_suit and (card.number == 11 and (card.suit == trump_suit or card.suit == trump_suit.opposite_suit_same_color())):
                self.hand_playable.append(card)
                


        #if no playable cards add all cards to playable
        if not len(self.hand_playable):
            for card in self.hand:
                self.hand_playable.append(card)

        return self.hand_playable

    def has_suit(self, leadsuit: Suit, trump_suit) -> bool:
        for card in self.hand:
            if card.suit == leadsuit and not (card.number == 11 and card.suit == trump_suit):
                return True
            if (trump_suit == Suit.HEARTS or trump_suit == Suit.DIAMONDS) and (card.number == 11 and (card.suit == Suit.HEARTS or card.suit == Suit.DIAMONDS)):
                return True
            if (trump_suit == Suit.SPADES or trump_suit == Suit.CLUBS) and (card.number == 11 and (card.suit == Suit.CLUBS or card.suit == Suit.SPADES)):
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
    
    def play_card(self, lead_card: Optional[Card], trump_suit: Suit) -> Card:
        """
        play_card plays a random card from the hand_playable
        
        lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        self.find_playable(lead_card, trump_suit)
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
        
class Player_MDP(Player):
    def __init__(self, name: str, hand: list[Card], deck: Deck) -> None:
        self.name = name
        self.hand = hand
        self.hand_playable = list[Card]()
        self.deck = deck
        self.score: int = 0
        self.in_play = list[Card]()
        self.seen = list[Card]()
        self.card_map = defaultdict(list)
        for card in hand:
            self.card_map[card.suit].append(card)    
    
    def play_card(self, lead_card: Optional[Card], trump_suit: Suit) -> Card:
        """
        play_card plays a card from the hand_playable
        
        lead_card: card that was played first if it is the first card in the trick lead_card is None
        """
        self.find_playable(lead_card, trump_suit)
        played_card = random.choice(self.hand_playable)
        self.hand.remove(played_card)


        player_cards = []
        for card in self.deck.cards:
            if card in self.in_play:
                player_cards.append("in_play")
            elif card in self.seen:
                player_cards.append("seen")
            elif card in self.hand:
                player_cards.append("m1")
                continue
            else:
                player_cards.append("m2")
        print(self.name + str(player_cards))
    
        return played_card
    
    def observeActionTaken(self, player, card: Card) -> None:
        if player == self:
            self.card_map[card.suit].remove(card)
        self.in_play.append(card) 

        #TODO: this should only happen when the trick is over change 4 to however many players there are
        if len(self.in_play) == 4:
            self.seen.extend(self.in_play)
            self.in_play.clear()
            self.lead_card = None