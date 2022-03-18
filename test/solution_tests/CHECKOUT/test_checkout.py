from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_valid_sum(self):
        assert checkout_solution.checkout("1A2B3C4D") == 215

if __name__ == "__main__":
    unittest.main()
