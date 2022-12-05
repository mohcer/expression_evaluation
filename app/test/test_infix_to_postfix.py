"""
Problem Domain : Test the infix to postfix conversion
"""
import unittest
from app.main.utils import infix_to_postfix

class TestInfixtoPostfix(unittest.TestCase):
    """
    Test different infix to postfix expressions
    """

    def test_infix_to_postfix(self):
        infix1 = "((15 / (7 - (1 + 1) ) ) * 3 ) - (2 + (1 + 1))"

        postfix = infix_to_postfix(infix1)

        self.assertEqual(postfix, "15  7  1  1+ - /  3 *  2  1  1++-")