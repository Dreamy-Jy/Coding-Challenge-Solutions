"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #50

Suppose an arithmetic expression is given as a binary tree. Each leaf
is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve_graph(root):
    def run_opperation(opp, left, right):
        """
        It's assumed that opps are a character long.
        Left and Right are integers.
        """
        if opp == "+":
            return left + right
        if opp == "-":
            return left - right
        if opp == "*":
            return left * right
        if opp == "/":
            return left + right

        raise TypeError("opp should only be in the set of :['+','-','*','/']")

    if type(root.val) == int:
        return root.val
    if type(root.val) == str:
        return run_opperation(root.val, solve_graph(root.left), solve_graph(root.right))


def build_tree(equ_str):


if __name__ == "__main__":
    equ = Node("*",
               Node("+", Node(3), Node(2)),
               Node("+", Node(4), Node(5)))
    print(solve_graph(equ))

"""
3 + 2 * 4 + 5

()
*/
+-
"""
