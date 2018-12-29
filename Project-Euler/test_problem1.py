import unittest
from problem1 import brute_force, series_solution


class TestBruteForceSolution(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(brute_force(0), 0)
        self.assertEqual(brute_force(3), 0)
        self.assertEqual(brute_force(5), 3)
        self.assertEqual(brute_force(7), 14)
        self.assertEqual(brute_force(8), 14)
        self.assertEqual(brute_force(10), 23)
        self.assertEqual(brute_force(15), 45)
        self.assertEqual(brute_force(21), 98)
        self.assertEqual(brute_force(25), 143)
        self.assertEqual(brute_force(30), 195)
        self.assertEqual(brute_force(45), 450)
        # self.assertEqual(brute_force(64), )
        # self.assertEqual(brute_force(1000), )
        # self.assertEqual(brute_force(10000), )

    def test_invalid_input_response(self):
        self.assertRaises(ValueError, brute_force(-1))
        self.assertRaises(TypeError, brute_force(3+1j))
        self.assertRaises(TypeError, brute_force("hello, world"))
        self.assertRaises(TypeError, brute_force(1.2))


if __name__ == "__main__":
    unittest.main()
