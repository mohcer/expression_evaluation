"""
Problem Domain: It describes all the models that describe Node Tree etc entities 
"""


class TreeNode:
    """
    It represents the tree node in a binary tree
    """
    def __init__(self, data) -> None:
        self.left = self.right = None

        self.data = data