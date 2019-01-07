import unittest
from problem1 import brute_force, one_pass_solution


class TestBruteForceSolution(unittest.TestCase):
    def test_correctness(self):
        """A test for wheither the brute force method returns the correct values"""
        self.assertEqual(brute_force([], 3), False)
        self.assertEqual(brute_force([1], 3), False)
        self.assertEqual(brute_force([1, 2], 3), True)
        self.assertEqual(brute_force([4, 2], 3), False)
        self.assertEqual(brute_force([3, 4, 8, 8], 16), True)
        self.assertEqual(brute_force([3, 4, 8, 8], 9), False)
        self.assertEqual(brute_force([0, 7, 3, 8, 7], 3), True)
        self.assertEqual(brute_force([6, 8, 6, 4, 9], 9), False)
        self.assertEqual(brute_force([-3, 4, 8, 8], 5), True)
        self.assertEqual(brute_force([-1, -2], -3), True)
        self.assertEqual(brute_force([-1, 0, 3, 5, -2], -3), True)

    def test_invalid_input_response(self):
        """A test for wheither the brute force method handles invalid input properily."""
        self.assertRaises(TypeError, brute_force, "Hello World", 9)
        self.assertRaises(TypeError, brute_force, 11, 9)
        self.assertRaises(TypeError, brute_force, 11.0, 9)
        self.assertRaises(TypeError, brute_force, 11+1j, 9)
        self.assertRaises(TypeError, brute_force, [
                          "H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"], 9)
        self.assertRaises(TypeError, brute_force, [11, 12, "s"], 9)
        self.assertRaises(TypeError, brute_force, [11.0, 13, 15], 9)
        self.assertRaises(TypeError, brute_force, [11+1j, 1, 23], 9)
        self.assertRaises(TypeError, brute_force, [True, 1, 23], 9)
        self.assertRaises(TypeError, brute_force, [3, 4, 8, 8], "W")
        self.assertRaises(TypeError, brute_force, [3, 4, 8, 8], 8.0)
        self.assertRaises(TypeError, brute_force, [3, 4, 8, 8], 11+5j)
        self.assertRaises(TypeError, brute_force, [3, 4, 8, 8], True)
        self.assertRaises(TypeError, brute_force, [3, 4, 8, 8], [1, 2, 3])


class TestOnePassSolution(unittest.TestCase):
    def test_correctness(self):
        """A test for wheither the one pass method returns the correct values"""
        self.assertEqual(one_pass_solution([], 3), False)
        self.assertEqual(one_pass_solution([1], 3), False)
        self.assertEqual(one_pass_solution([1, 2], 3), True)
        self.assertEqual(one_pass_solution([4, 2], 3), False)
        self.assertEqual(one_pass_solution([3, 4, 8, 8], 16), True)
        self.assertEqual(one_pass_solution([3, 4, 8, 8], 9), False)
        self.assertEqual(one_pass_solution([0, 7, 3, 8, 7], 3), True)
        self.assertEqual(one_pass_solution([6, 8, 6, 4, 9], 9), False)
        self.assertEqual(one_pass_solution([-3, 4, 8, 8], 5), True)
        self.assertEqual(one_pass_solution([-1, -2], -3), True)
        self.assertEqual(one_pass_solution([-1, 0, 3, 5, -2], -3), True)

    def test_invalid_input_response(self):
        """A test for wheither the one pass method handles invalid input properily."""
        self.assertRaises(TypeError, one_pass_solution, "Hello World", 9)
        self.assertRaises(TypeError, one_pass_solution, 11, 9)
        self.assertRaises(TypeError, one_pass_solution, 11.0, 9)
        self.assertRaises(TypeError, one_pass_solution, 11+1j, 9)
        self.assertRaises(TypeError, one_pass_solution, [
                          "H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"], 9)
        self.assertRaises(TypeError, one_pass_solution, [11, 12, "s"], 9)
        self.assertRaises(TypeError, one_pass_solution, [11.0, 13, 15], 9)
        self.assertRaises(TypeError, one_pass_solution, [11+1j, 1, 23], 9)
        self.assertRaises(TypeError, one_pass_solution, [True, 1, 23], 9)
        self.assertRaises(TypeError, one_pass_solution, [3, 4, 8, 8], "W")
        self.assertRaises(TypeError, one_pass_solution, [3, 4, 8, 8], 8.0)
        self.assertRaises(TypeError, one_pass_solution, [3, 4, 8, 8], 11+5j)
        self.assertRaises(TypeError, one_pass_solution, [3, 4, 8, 8], True)
        self.assertRaises(TypeError, one_pass_solution,
                          [3, 4, 8, 8], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
