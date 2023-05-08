from cards import Card, Deck
from typing import Optional, List, Tuple
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = list[Card]()
        self.hand_playable = list[Card]()
        self.score: int = 0
        self.deck = []


        self.state = []
        self.actions = []
        self.action = 0
        
    def find_playable(self, lead_card: Optional[Card]) -> List[Card]:
        """
        Looks at hand and finds playable cards, then adds them to hand_play
        lead_card: card that was played first if first card in trick lead_card is None
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

    def identify_state(self, deck: Deck) -> None:
        """
        Identifies the state of the player
        """
        #state = [lead_card, hand_playable, hand, score]
        # [self.hand_playable, self.hand, self.score] in future ?
        for card in deck.cards:
            if card in self.hand_playable:
                self.state.append(1)
            else:
                self.state.append(0)
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