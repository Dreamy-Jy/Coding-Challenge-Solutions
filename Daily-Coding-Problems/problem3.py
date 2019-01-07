'''
Daily Coding Problem: Problem #3

Given the root to a binary tree,
implement serialize(root), which serializes
the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

Can you do this without recursion?
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO get rid of the trailing white space
def preorder_serialize(head: Node, seperator: str = " ", ender: str = "|") -> str:
    if head == None:
        return ""
    if head.right == None and head.left == None:
        return str(head.val) + seperator + ender + seperator

    return str(head.val) + seperator + preorder_serialize(head.left, seperator) + preorder_serialize(head.right, seperator)


# NOTE I'm considering adding a type denoter
def preorder_deserialize(string_rep: str) -> Node:
    pass


def postorder_serialize(head: Node) -> str:
    pass


def postorder_deserialize(string_rep: str) -> Node:
    pass


def inorder_serialize(head: Node) -> str:
    pass


def inorder_deserialize(string_rep: str) -> Node:
    pass


def levelorder_serialize(head: Node) -> str:
    pass


def levelorder_deserialize(string_rep: str) -> Node:
    pass


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert preorder_deserialize(preorder_serialize(
        node)).left.left.val == 'left.left'
'''
    assert postorder_deserialize(
        postorder_serialize(node)).left.left.val == 'left.left'

    assert inorder_deserialize(
        inorder_serialize(node)).left.left.val == 'left.left'

    assert levelorder_deserialize(
        levelorder_serialize(node)).left.left.val == 'left.left'
'''
