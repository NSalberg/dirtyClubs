import unittest
import game as gm

class TestBidding(unittest.TestCase):
    # write a test case for the getHighestBidder function
    def test_getHighestBidder(self):
        # create a game with 4 players
        players = [gm.Player("Player 1"), gm.Player("Player 2"), gm.Player("Player 3"), gm.Player("Player 4")]
        game = gm.Game(players, gm.Deck([1,9,10,11,12,13]), 5)
        # set the highest bid to 3 and the highest bidder to the first player
        game.getHighestBidder(0)
        self.assertEqual(gm.highestBid, 3)
        self.assertEqual(gm.highestBidder, gm.players[0])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBidding))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()