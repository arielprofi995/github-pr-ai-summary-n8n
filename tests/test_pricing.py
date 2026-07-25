"""Testy funkcji obliczającej wartość zamówienia."""

import unittest

from src.pricing import calculate_total


class CalculateTotalTests(unittest.TestCase):
    """Testy podstawowego kalkulatora cen."""

    def test_calculates_total_with_default_tax(self):
        result = calculate_total(100.00)

        self.assertEqual(result, 123.00)

    def test_calculates_total_with_custom_tax(self):
        result = calculate_total(200.00, tax_rate=0.08)

        self.assertEqual(result, 216.00)

    def test_rejects_negative_subtotal(self):
        with self.assertRaises(ValueError):
            calculate_total(-10.00)

    def test_rejects_negative_tax_rate(self):
        with self.assertRaises(ValueError):
            calculate_total(100.00, tax_rate=-0.10)


if __name__ == "__main__":
    unittest.main()
