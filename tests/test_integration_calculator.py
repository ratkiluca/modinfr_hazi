import unittest
from calculator import Calculator


class TestCalculatorIntegration(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_combined_operations(self) -> None:
        """_summary_
        """
        calc = Calculator()
        result = calc.add(a=1, b=2)
        result = calc.multiply(a=result, b=10)
        self.assertEqual(first=result, second=30)
