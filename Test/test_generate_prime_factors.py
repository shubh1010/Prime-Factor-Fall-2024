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


if __name__ == '__main__':
    unittest.main()