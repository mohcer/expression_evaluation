"""
Problem Domain: Test all operations related to expression tree
"""

import unittest
from app.main.model import ExpressionTree
from app.main.utils import infix_to_postfix

class TestExpressionTree(unittest.TestCase):
    """
    Test all expression tree functions
    """
    exp_tree = ExpressionTree()

    def test_create_expression_tree(self):
        infix_exp = "((15 / (7 - (1 + 1) ) ) * -3 ) - (2 + (1 + 1))"
        postfix_exp = infix_to_postfix(infix_exp)

        self.exp_tree.generate_exp_tree(postfix_exp)

        self.exp_tree.display_tree(self.exp_tree.root_node)

