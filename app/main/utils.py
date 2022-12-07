"""
Problem Domain: defines all the util functions
"""
import re

OPERATORS = set(['+', '-', '*', '/', '(', ')','^'])
PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

def tokenize_string(input_str: str):
    """
    :purpose: for the given input string it tokenizes and creates a list of chars
    """
    return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", input_str)
        
def infix_to_postfix(infix_exp: str) -> str:
    """
    :purpose: for the give infix_expression converts it to a postfix expression
    """
    stack = []

    postfix_exp = ''
    
    for idx, chr in enumerate(infix_exp):
        if chr not in OPERATORS:
            # if chr is an operand append it to the postfix_exp string
            postfix_exp += chr
        elif chr == '(':
            # opening parenthesis push to stack
            stack.append(chr)
        elif chr == ')':
            # for closing parenthesis pop from stack until find opening parenthesis
            # append it to the postfix expr
            while stack and stack[-1] != '(':
                postfix_exp += stack.pop()
            
            # pop the '('
            stack.pop()
        else: 
            # pop and append to postfix exp until the top 
            while stack and stack[-1] != '(' and PRIORITY[chr] <= PRIORITY[stack[-1]]:
                postfix_exp += stack.pop()
        
            stack.append(chr)
    
    while stack: 
        postfix_exp += stack.pop()
    
    return postfix_exp