import unittest
from trouble_sort import trouble_sort, find_sort_error, check_trouble_sort

class TestTroubleSort(unittest.TestCase):
    def test_sort(self):
        """ Test that the sort returns the expected array"""
        self.assertEqual(trouble_sort([8, 9, 7]), [7, 9, 8])
        self.assertEqual(trouble_sort([5, 6, 6, 4, 3]), [3, 4, 5, 6, 6])

class TestFindSortError(unittest.TestCase):
    def test_error(self):
        """ Test that the method returns the expected index"""
        self.assertEqual(find_sort_error([7, 9, 8]), 1)
        self.assertEqual(find_sort_error([3, 4, 5, 6, 6]), -1)
        self.assertEqual(find_sort_error([8, 9, 7]), 1)
        self.assertEqual(find_sort_error([4, 5, 6, 6, 3]), 3)

class TestCheckTroubleSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(check_trouble_sort([5, 6, 8, 4, 3]), 'OK')
        self.assertEqual(check_trouble_sort([8, 9, 7]), 1)