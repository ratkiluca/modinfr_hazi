import unittest
from calculator import Calculator


class TestCalculatorUnit(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_add(self) -> None:
        """
        Testing possible edge cases
        """
        # Test zeros
        self.assertEqual(first=self.calc.add(a=0, b=0), second=0)
        # Test negatives
        self.assertEqual(first=self.calc.add(a=-1, b=1), second=0)
        # Test floats
        self.assertEqual(first=self.calc.add(a=1.5, b=2.5), second=4.0)

    def test_subtract(self) -> None:
        """
        Testing possible edge cases
        """
        self.assertEqual(first=self.calc.subtract(a=10, b=5), second=5)
        self.assertEqual(first=self.calc.subtract(a=5, b=10), second=-5)

    def test_multiply(self) -> None:
        """
        Testing possible edge cases
        """
        # Test zero
        self.assertEqual(first=self.calc.multiply(a=0, b=5), second=0)
        # Test negatives
        self.assertEqual(first=self.calc.multiply(a=-2, b=3), second=-6)

    def test_divide(self) -> None:
        """
        Testing possible edge cases
        """
        # Simple test
        self.assertEqual(first=self.calc.divide(a=10, b=2), second=5.0)
        # Test negatives
        self.assertEqual(first=self.calc.divide(a=-10, b=2), second=-5.0)
        # Test division by zero
        self.assertRaises(ValueError, self.calc.divide, 5, 0)
