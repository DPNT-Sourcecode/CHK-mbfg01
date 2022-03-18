from lib.solutions.CHK import checkout_solution
import unittest


class TestSum(unittest.TestCase):
    def test_valid_1(self):
        assert checkout_solution.checkout("FF") == 20

    def test_valid_2(self):
        assert checkout_solution.checkout("ABCDEF") == 165

    def test_valid_3(self):
        assert checkout_solution.checkout("AAAAAAA") == 300

    def test_valid_4(self):
        assert checkout_solution.checkout("AAAAAAAFF") == 320

    def test_valid_5(self):
        assert checkout_solution.checkout("AAAAAAAF") == 310

    def test_valid_6(self):
        assert checkout_solution.checkout("AAAAAAAFFFFF") == 330

    def test_valid_sum(self):
        assert checkout_solution.checkout("ABCDE") == 155

    def test_invalid(self):
        assert checkout_solution.checkout("F") == 10

    def test_invalid_digit(self):
        assert checkout_solution.checkout("AX") == -1

    def test_invalid_digitest_zerot(self):
        assert checkout_solution.checkout("") == 0

    def test_invalid_digitest_one(self):
        assert checkout_solution.checkout("123") == -1

if __name__ == "__main__":
    unittest.main()


