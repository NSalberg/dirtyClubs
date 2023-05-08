import unittest

from cards import Card, Deck
from players import Player
from turn import Turn

class TestCard(unittest.TestCase):
    def test_same_card(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Hearts", 1)
        self.assertEqual(card1, card2)
    def test_different_number(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Hearts", 2)
        self.assertNotEqual(card1, card2)
    def test_different_suit(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Spades", 1)
        self.assertNotEqual(card1, card2)
    def test_card_and_none(self):    
        card1 = Card("Hearts", 1)
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
    def test_player_hand(self):
        player = Player("Bob")
        self.assertEqual(len(player.hand), 0)

    def test_playable_none(self):
        player = Player("Bob")
        cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 10)]
        player.hand = cards
        playable_cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 10)]
        find_playable_cards = player.find_playable(lead_card=None)
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_hearts(self):
        player = Player("Bob")
        cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 10)]
        player.hand = cards
        playable_cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11)]
        find_playable_cards = player.find_playable(lead_card=Card("Hearts", 1))
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_spades(self):
        player = Player("Bob")
        cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 10)]
        player.hand = cards
        playable_cards = [Card("Spades", 10)]
        find_playable_cards = player.find_playable(lead_card=Card("Spades", 1))
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_clubs(self):
        player = Player("Bob")
        cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 10)]
        player.hand = cards
        playable_cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 10)]
        find_playable_cards = player.find_playable(lead_card=Card("Clubs", 1))
        self.assertEqual(playable_cards, find_playable_cards)

    def test_playable_opposite_color_jack(self):
        player = Player("Bob")
        cards = [Card("Hearts", 1), Card("Hearts", 9), Card("Hearts", 10), Card("Hearts", 11), Card("Spades", 11)]
        player.hand = cards
        playable_cards = [Card("Spades", 11)]
        find_playable_cards = player.find_playable(lead_card=Card("Clubs", 1))
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