"""
Problem Domain: It describes all the models that describe TreeNode, ExpressionTree etc entities 
"""
import re

class TreeNode:
    """
    It represents the tree node in a binary tree
    """
    def __init__(self, data) -> None:
        self.left_ref = self.right_ref = None

        self.data = data

class ExpressionTree:
    """
    It represents an Expression Tree class
    """
    def __init__(self) -> None:
        self.__root_node = None
    
    @property
    def root_node(self):
        return self.__root_node

    def check_isoperator(self, char) -> bool:
        """
        :purpose: for the given charachter check if it is an operator
        return True if found False otherwise
        """
        return char in [" ", "+", "-", "*", "/", "^"]

    def check_if_leafnode(node: TreeNode) -> bool:
        """
        :purpose: for the given node check if its a leaf node
        """
        return node.left_ref is None and node.right_ref is None

    def tokenize_string(self, input_str: str):
        """
        :purpose: for the given input string it tokenizes and creates a list of chars
        """
        return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", input_str)

    def generate_exp_tree(self, postfix_exp):
        """
        :purpose: from the postfix_exp it generates the expression tree
        """
        stack = []

        print(f"Inside generaate tree")
        print(postfix_exp)
        # In postfix expression the operators will always be last
        # and the last operator is the root element
        self.__root_node = TreeNode(postfix_exp[-1])

        stack.append(self.__root_node)

        # traverse the remaining exp from the right end
        # reverse the exp
        temp_exp = list(reversed(self.tokenize_string(postfix_exp[:-1])))
        
        for exp_chr in temp_exp:
            top_node = stack[-1]
        
            temp_node = TreeNode(exp_chr)
            if top_node.right_ref is None:
                top_node.right_ref = temp_node

                # also check if its an operator, then push it to the stack
                if self.check_isoperator(exp_chr):
                    stack.append(temp_node)
            else:
                top_node.left_ref = temp_node

                stack.pop(-1)

                if self.check_isoperator(exp_chr):
                    stack.append(temp_node)
            
            print(f"stack : {stack}")

    def process_sub_exp(self, op, a, b):
        """
        :purpose: for the given operator op applies it to the given operands and returns the result
        """
        sub_exp_val = 0

        if op == '+':
            sub_exp_val = a + b
        elif op == '-':
            sub_exp_val = a - b
        elif op == '*':
            sub_exp_val = a * b
        elif op == '/':
            sub_exp_val = a / b
        elif op == '^':
            sub_exp_val = pow(a, b)
        
        return sub_exp_val

    def evaluate_expression_tree(self, node: TreeNode) -> float:
        """
        :purpose: from the constructed expression tree it evaluates the expression and returns the result value 
        """
        if node is None:
            return 0
        
        if self.check_if_leafnode(node):
            return float(node.data)
        
        a = self.evaluate_expression_tree(node.left_ref)
        b = self.evaluate_expression_tree(node.right_ref)

        return self.process_sub_exp(node.data, a, b)

    def display_tree(self, root):
        """
        :purpose: It displays the constructed expression tree by doing an inorder traversal
        """
        def height(root):
            return 1 + max(height(root.left_ref), height(root.right_ref)) if root else -1 

        nlevels = height(root)
        width =  pow(2,nlevels+1)

        q=[(root,0,width,'c')]
        levels=[]

        while(q):
            node,level,x,align= q.pop(0)
            if node:            
                if len(levels)<=level:
                    levels.append([])
            
                levels[level].append([node,level,x,align])
                seg= width//(pow(2,level+1))
                q.append((node.left_ref,level+1,x-seg,'l'))
                q.append((node.right_ref,level+1,x+seg,'r'))

        for i,l in enumerate(levels):
            pre=0
            preline=0
            linestr=''
            pstr=''
            seg= width//(pow(2,i+1))
            for n in l:
                valstr= str(n[0].data)
                if n[3]=='r':
                    linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                    preline = n[2] 
                if n[3]=='l':
                    linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                    preline = n[2] + seg + seg//2
                pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr) 
        
