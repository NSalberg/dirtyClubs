import unittest

from cards import Card, Deck, Suit
from players import Player, Player_Random
from game import ClubsEngine

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

class TestGame(unittest.TestCase):
    deck = Deck([9,10,11,12,13,14])
    num_players = 4
    game = ClubsEngine(num_players, deck, 5, True)

    def test_find_winner_jack(self):
        in_play = [Card(Suit.HEARTS, 14), Card(Suit.HEARTS, 9), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11)]
        self.assertEqual(self.game.find_winner(in_play, Suit.HEARTS), 3 )

    def test_find_winner_opposite_jack(self):
        in_play = [Card(Suit.HEARTS, 14), Card(Suit.DIAMONDS, 11), Card(Suit.HEARTS, 9), Card(Suit.HEARTS, 10) ]
        self.assertEqual(self.game.find_winner(in_play, Suit.HEARTS), 1 )
        
    def test_find_winner_lead_suit(self):
        in_play = [Card(Suit.HEARTS, 9), Card(Suit.HEARTS, 14), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11)]
        self.assertEqual(self.game.find_winner(in_play, Suit.SPADES), 1 )

    def test_find_winner_trump(self):
        in_play = [Card(Suit.HEARTS, 14), Card(Suit.CLUBS, 9), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11)]
        self.assertEqual(self.game.find_winner(in_play, Suit.CLUBS), 1 )

    def test_find_winner_trump_opposite_jack(self):
        in_play = [Card(Suit.HEARTS, 14), Card(Suit.SPADES, 11), Card(Suit.HEARTS, 10), Card(Suit.HEARTS, 11)]
        self.assertEqual(self.game.find_winner(in_play, Suit.CLUBS), 1 )
    def test_find_winner(self):
        in_play = [Card(Suit.SPADES, 13), Card(Suit.SPADES, 10), Card(Suit.HEARTS, 14), Card(Suit.SPADES, 11)]
        self.assertEqual(self.game.find_winner(in_play, Suit.CLUBS), 3 )
    
def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCard))
    test_suite.addTest(unittest.makeSuite(TestDeck))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestGame))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

if __name__ == "__main__":
    run_tests()