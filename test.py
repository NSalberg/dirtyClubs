import unittest
import game as gm
from io import StringIO
import sys


class TestBidding(unittest.TestCase):
    # write a test case for the getHighestBidder function
    def test_getHighestBidder(self):
        # create a game with 4 players
        players = [gm.Player("Player 1"), gm.Player("Player 2"), gm.Player("Player 3"), gm.Player("Player 4")]
        game = gm.Game(players, gm.Deck([1,9,10,11,12,13]), 5)
        input = StringIO("5\n2\n3\n4\n0\n")
        sys.stdin = input
        
        
        # set the highest bid to 5 and the highest bidder to the first player
        highestBid , highestBidder = game.getHighestBidder(0)
        sys.stdin.getvalue().strip()
        self.assertEqual(highestBid, 5)
        self.assertEqual(highestBidder, game.players[1])
        

        # have the player 4 bid 4 
        highestBid , highestBidder = game.getHighestBidder(0)
        self.assertEqual(highestBid, 4)
        self.assertEqual(highestBidder, game.players[3])

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestBidding))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

if __name__ == "__main__":
    run_tests()