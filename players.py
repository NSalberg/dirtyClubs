from cards import Card
from typing import Optional

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = list[Card]()
        self.hand_playable = list[Card]()
        self.score: int = 0


        self.state = dict()
        self.actions = dict()
        self.action = 0
        
    def find_playable(self, lead_card: Optional[Card]) -> None:
        """
        Looks at hand and finds playable cards, then adds them to hand_play
        lead_card: card that was played first if first card in trick lead_card is None
        """
        self.hand_playable = list[Card]()
        #if lead_card is None or player does not have suit of lead_card add all cards to playable
        if lead_card is None or not self.has_suit(lead_card.suit):
            for card in self.hand:
                self.hand_playable.append(card)
        else:
            for card in self.hand:
                if  card.suit == lead_card.suit:
                    self.hand_playable.append(card)

    
    def has_suit(self, suit: str) -> bool:
        for card in self.hand:
            if card.suit == suit:
                return True
        return False

    def __eq__(self, player: object) -> bool:
        if isinstance(player, Player):
            return self.name == player.name
        return False