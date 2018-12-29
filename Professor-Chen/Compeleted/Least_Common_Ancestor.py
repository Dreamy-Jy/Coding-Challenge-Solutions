import random
"""
    Q.6 Find the least common ancestor (LCA) of two nodes in a binary search tree
    Please read the key vector {500,300,600,550,700,750,200,150,250,350,800}
    Pick up two random keys and show their LCA
"""
test_tree = [500, 300, 600, 550, 700, 750, 200, 150, 250, 350, 800]

rand_one = random.randint(0, len(test_tree))
rand_two = random.randint(0, len(test_tree))

"""
NOTE: why do the loop by dept instead of index and check if the index is the range for that number.
TODO: Add error handling
"""


def getDepth(index):
    """Returns the dept of an value in an heap, starting with 0"""
    depth_end = 0
    depth = 0

    for i in range(index + 1):
        if i > depth_end:
            depth = depth + 1
            depth_end += 2**depth
    return depth


def getParentIndex(index):
    """Returns a parent Index for a given node"""
    if index == 0:
        return 0

    return int(index - (index // 2) - 1)


def getLeastCommonAncestor(index_a, index_b):
    """Given the two indexs of nodes in a heap, this method returns their least common ancestor"""
    a_parent = getParentIndex(index_a)
    b_parent = getParentIndex(index_b)

    if a_parent == b_parent:
        return a_parent

    if a_parent == 0 or b_parent == 0:
        return 0

    if getDepth(a_parent) == getDepth(b_parent):
        return getLeastCommonAncestor(a_parent, b_parent)
    elif getDepth(a_parent) < getDepth(b_parent):
        return getLeastCommonAncestor(index_a, b_parent)
    elif getDepth(a_parent) > getDepth(b_parent):
        return getLeastCommonAncestor(a_parent, index_b)
