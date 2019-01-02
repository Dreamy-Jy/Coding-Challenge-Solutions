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

    def test_invalid_input_response(self):
        self.assertRaises(ValueError, brute_force, -1)
        self.assertRaises(TypeError, brute_force, 3+1j)
        self.assertRaises(TypeError, brute_force, "hello, world")
        self.assertRaises(TypeError, brute_force, 1.2)


class TestSeriesSolution(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(series_solution(0), 0)
        self.assertEqual(series_solution(3), 0)
        self.assertEqual(series_solution(5), 3)
        self.assertEqual(series_solution(7), 14)
        self.assertEqual(series_solution(8), 14)
        self.assertEqual(series_solution(10), 23)
        self.assertEqual(series_solution(15), 45)
        self.assertEqual(series_solution(21), 98)
        self.assertEqual(series_solution(25), 143)
        self.assertEqual(series_solution(30), 195)
        self.assertEqual(series_solution(45), 450)

    def test_invalid_input_response(self):
        self.assertRaises(ValueError, series_solution, -1)
        self.assertRaises(TypeError, series_solution, 3+1j)
        self.assertRaises(TypeError, series_solution, "hello, world")
        self.assertRaises(TypeError, series_solution, 1.2)


if __name__ == "__main__":
    unittest.main()
