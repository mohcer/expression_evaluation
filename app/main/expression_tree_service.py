"""
Problem Domain: This service represents all the operations that 
takes expression as input from user and outputs the evaluation result 
"""
from app.main.model import ExpressionTree
from app.main.utils import infix_to_postfix

class ExpressionTreeService:
    """
    :purpose: It declares the below operation as an Expression tree service
    1) Display Tree
    2) Expression Evualation Result
    """
    def __init__(self, infix_exp) -> None:
        self.__infix_exp = infix_exp
        self.__exp_tree = ExpressionTree()

        # Algo
        # 1) convert infix to postfix
        # 2) generate tree using the postfix
        postfix_exp = infix_to_postfix(self.__infix_exp)

        self.__exp_tree.generate_exp_tree(postfix_exp)

    def evaluate_expression(self):
        # 3) evaluate the value of expression by tree traversal
        return self.__exp_tree.evaluate_expression_tree(self.__exp_tree.root_node)


    def display_tree(self):
        self.__exp_tree.display_tree(self.__exp_tree.root_node)


if __name__ == '__main__':
    infix_exp = input("\n Please enter the expression string : ")

    expression_tree_service = ExpressionTreeService(infix_exp)
    print("\n The Expression Tree is created successfully! \n")
    
    while True:
        print("\n1) Evaluate Expression \n")
        print("2) Display Expression Tree \n")
        print("3) Exit \n")

        input_option = input("Please Enter your choice : ")

        if int(input_option) == 1:
            print(f"\n Choice entered : Evaluate Expression")
            res = expression_tree_service.evaluate_expression()
            print(f"\n The result of expression : {res}")
        elif int(input_option) == 2:
            print(f"\n Choice entered : Display Expression Tree")
            expression_tree_service.display_tree()
        elif int(input_option) == 3:
            exit(0)
        else:
            print("\n You entered an invalid choice please input correct choice!")





