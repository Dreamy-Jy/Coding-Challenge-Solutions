"""
🌩Dreamy-Jy🌩 back at it again ⚡️...

Daily Coding Problem: Problem #24

Implement locking in a binary tree. A binary tree node can be locked or unlocked only 
if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    - `is_locked`, which returns whether the node is locked
    
    - `lock`, which attempts to lock the node. If it cannot
    be locked, then it should return false. Otherwise, it
    should lock it and return true.
    
    - `unlock`, which unlocks the node. If it cannot be unlocked,
    then it should return false. Otherwise, it should unlock it
    and return true.

You may augment the node to add parent pointers or any other property you would like. You
may assume the class is used in a single-threaded program, so there is no need for actual
locks or mutexes. Each method should run in O(h), where h is the height of the tree.

NOTE
not fully solved but many of the concepts are correct...
What are locks and mutexes?

"""


class LockableNode(object):

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False

    def unlock(self):
        if LockableNode._is_unlockable(self):
            self.locked = False
            return True
        return False

    def lock(self):
        if LockableNode._is_lockable(self):
            self.locked = True
            return True
        return False

    def is_locked(self):
        return self.locked

    @staticmethod
    def _is_lockable(node):
        if None:
            return True
        if node.locked:
            return False
        return LockableNode._is_lockable(node.left) and LockableNode._is_lockable(node.right)

    @staticmethod
    def _is_unlockable(node):
        current = node
        while current.parent != None:
            if current.locked:
                return False
            current = current.parent
        return True
