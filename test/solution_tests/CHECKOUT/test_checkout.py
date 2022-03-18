from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_valid_sum(self):
        assert checkout_solution.checkout("ABBCCCDDD") == 215

    def test_valid_sum(self):
        assert checkout_solution.checkout("AAABBCD") == 210

    def test_invalid(self):
        assert checkout_solution.checkout("ASDF") == -1

    def test_invalid_digit(self):
        assert checkout_solution.checkout("AX") == -1

    def test_invalid_digitest_zerot(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid_digitest_one(self):
        assert checkout_solution.checkout("123") == -1

if __name__ == "__main__":
    unittest.main()
