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

        self.assertEqual(self.exp_tree.root_node.data, postfix_exp[-1])

    def test_evaluate_expression_tree(self):
        infix_exp = "(1 * 5) + (3 / 10)"
        postfix_exp = infix_to_postfix(infix_exp)
        
        self.exp_tree.generate_exp_tree(postfix_exp)
        
        res = self.exp_tree.evaluate_expression_tree(self.exp_tree.root_node)

        self.assertEqual(res, 5.3)
    
    def test_evaluste_complex_expression(self):
        infix_exp = "((15 / (7 - (1 + 1) ) ) * 3 ) - (2 + (1 + 1))"
        postfix_exp = infix_to_postfix(infix_exp)
        
        self.exp_tree.generate_exp_tree(postfix_exp)
        
        res = self.exp_tree.evaluate_expression_tree(self.exp_tree.root_node)

        self.assertEqual(res, 5.0)

