import unittest
from prime import generate_prime_factors


class TestPrimeFactors(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_prime_factors("string")
        with self.assertRaises(ValueError):
            generate_prime_factors(4.5)

    def test_input_is_1(self):
        self.assertEqual(generate_prime_factors(1), [])

    def test_input_is_2(self):
        self.assertEqual(generate_prime_factors(2), [2])

    def test_input_is_3(self):
        self.assertEqual(generate_prime_factors(3), [3])

    def test_input_is_4(self):
        self.assertEqual(generate_prime_factors(4), [2, 2])

    def test_input_is_6(self):
        self.assertEqual(generate_prime_factors(6), [2, 3])

    def test_input_is_8(self):
        self.assertEqual(generate_prime_factors(8), [2, 2, 2])

    def test_input_is_9(self):
        self.assertEqual(generate_prime_factors(9), [3, 3])


if __name__ == '__main__':
    unittest.main()