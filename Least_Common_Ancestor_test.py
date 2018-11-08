import unittest
from Least_Common_Ancestor import *


class TestGetDepth(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(getDepth(0), 0)
        self.assertEqual(getDepth(1), 1)
        self.assertEqual(getDepth(2), 1)
        self.assertEqual(getDepth(3), 2)
        self.assertEqual(getDepth(4), 2)
        self.assertEqual(getDepth(5), 2)
        self.assertEqual(getDepth(6), 2)
        self.assertEqual(getDepth(7), 3)
        self.assertEqual(getDepth(8), 3)
        self.assertEqual(getDepth(9), 3)
        self.assertEqual(getDepth(10), 3)
        self.assertEqual(getDepth(11), 3)
        self.assertEqual(getDepth(12), 3)
        self.assertEqual(getDepth(13), 3)
        self.assertEqual(getDepth(14), 3)


class TestGetParentIndex(unittest.TestCase):
    def test_correctness(self):
        """This test that the method returns correct values."""
        self.assertEqual(getParentIndex(0), 0)
        self.assertEqual(getParentIndex(1), 0)
        self.assertEqual(getParentIndex(2), 0)
        self.assertEqual(getParentIndex(3), 1)
        self.assertEqual(getParentIndex(4), 1)
        self.assertEqual(getParentIndex(5), 2)
        self.assertEqual(getParentIndex(6), 2)
        self.assertEqual(getParentIndex(7), 3)
        self.assertEqual(getParentIndex(8), 3)
        self.assertEqual(getParentIndex(9), 4)
        self.assertEqual(getParentIndex(10), 4)
        self.assertEqual(getParentIndex(11), 5)
        self.assertEqual(getParentIndex(12), 5)
        self.assertEqual(getParentIndex(13), 6)
        self.assertEqual(getParentIndex(14), 6)

    
"""     def test_type(self):
        pass
    
    def test_values(self):
        pass """


class TestGetLeastCommonAncestor(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(getLeastCommonAncestor(7,8), 3)
        self.assertEqual(getLeastCommonAncestor(3,10), 1)
        self.assertEqual(getLeastCommonAncestor(0,0), 0)
        self.assertEqual(getLeastCommonAncestor(3,14), 0)
        self.assertEqual(getLeastCommonAncestor(0,14), 0)