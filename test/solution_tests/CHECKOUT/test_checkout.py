from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_valid_sum(self):
        assert checkout_solution.checkout("1A2B3C4D") == 215

    def test_valid_sum(self):
        assert checkout_solution.checkout("1A2B3C4D") == 215

    def test_invalid(self):
        assert checkout_solution.checkout("1A2B3C4E") == -1

    def test_invalid_digit(self):
        assert checkout_solution.checkout("-A2B3C4E") == -1

if __name__ == "__main__":
    unittest.main()

