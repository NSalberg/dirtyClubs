import unittest

from cards import Card, Deck, Suit
from players import Player_Random


class TestCard(unittest.TestCase):
    def test_same_card(self):
        card1 = Card(Suit.SPADES, 1)
        card2 = Card(Suit.SPADES, 1)
        self.assertEqual(card1, card2)
    def test_different_number(self):
        card1 = Card(Suit.HEARTS, 1)
        card2 = Card(Suit.HEARTS, 2)
        self.assertNotEqual(card1, card2)
    def test_different_suit(self):
        card1 = Card(Suit.HEARTS, 1)
        card2 = Card(Suit.SPADES, 1)
        self.assertNotEqual(card1, card2)
    def test_card_and_none(self):    
        card1 = Card(Suit.HEARTS, 1)
        card2 = None
        self.assertNotEqual(card1, card2)


class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    def test_shuffle_deck(self):
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(original_order, deck.cards)
    def test_draw_card(self):
        deck = Deck()
        card = deck.draw()
        self.assertEqual(len(deck.cards), 51)
    def test_draw_card_is_card(self):
        deck = Deck()
        card = deck.draw()
        self.assertIsInstance(card, Card)
    def test_custom_deck_size(self):
        deck = Deck(range=[1,2,3])
        self.assertEqual(len(deck.cards), 12)

class TestPlayer(unittest.TestCase):
    test_cards = [Card(Suit.HEARTS, 1), Card(Suit.HEARTS, 9), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11), Card(Suit.SPADES, 10)]
    
    def test_player_hand(self):
        player = Player_Random("Bob", [])
        self.assertEqual(len(player.hand), 0)

    def test_playable_none(self):
        cards = self.test_cards 
        player = Player_Random("Bob", cards)
        player.hand = cards
        playable_cards = self.test_cards 
        find_playable_cards = player.find_playable(lead_card=None)
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_hearts(self):
        cards = self.test_cards 
        player = Player_Random("Bob", cards)
        player.hand = cards
        playable_cards = [Card(Suit.HEARTS, 1), Card(Suit.HEARTS, 9), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11)]
        find_playable_cards = player.find_playable(lead_card=Card(Suit.HEARTS, 1))
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_spades(self):
        cards = self.test_cards 
        player = Player_Random("Bob", cards)
        player.hand = cards
        playable_cards = [Card(Suit.SPADES, 10)]
        find_playable_cards = player.find_playable(lead_card=Card(Suit.SPADES, 1))
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_clubs(self):
        cards = self.test_cards 
        player = Player_Random("Bob", cards)
        player.hand = cards
        playable_cards = self.test_cards 
        find_playable_cards = player.find_playable(lead_card=Card(Suit.CLUBS, 1))
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_opposite_color_jack(self):
        cards = [Card(Suit.HEARTS, 1), Card(Suit.HEARTS, 9), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11), Card(Suit.SPADES, 11)]
        player = Player_Random("Bob", cards)
        playable_cards = [Card(Suit.SPADES, 11)]
        find_playable_cards = player.find_playable(lead_card=Card(Suit.CLUBS, 1))
        self.assertEqual(playable_cards, find_playable_cards)
    
def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCard))
    test_suite.addTest(unittest.makeSuite(TestDeck))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

if __name__ == "__main__":
    run_tests()