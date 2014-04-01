import unittest

from numbers_problem import *


class NumbersStateTest(unittest.TestCase):
    def testShiftEmptySpaces(self):
        state = NumbersState.from_table(
            [[0, 0, 0, 2],
             [0, 0, 4, 0],
             [0, 8, 0, 0],
             [16, 0, 0, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(2, right.cell_at((0, 3)))
        self.assertEqual(4, right.cell_at((1, 3)))
        self.assertEqual(8, right.cell_at((2, 3)))
        self.assertEqual(16, right.cell_at((3, 3)))
        for row in range(4):
            for col in range(3):
                self.assertEqual(0, right.cell_at((row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(2, left.cell_at((0, 0)))
        self.assertEqual(4, left.cell_at((1, 0)))
        self.assertEqual(8, left.cell_at((2, 0)))
        self.assertEqual(16, left.cell_at((3, 0)))
        for row in range(4):
            for col in range(1, 4):
                self.assertEqual(0, left.cell_at((row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(2, up.cell_at((0, 3)))
        self.assertEqual(4, up.cell_at((0, 2)))
        self.assertEqual(8, up.cell_at((0, 1)))
        self.assertEqual(16, up.cell_at((0, 0)))
        for row in range(1, 4):
            for col in range(4):
                self.assertEqual(0, up.cell_at((row, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(2, down.cell_at((3, 3)))
        self.assertEqual(4, down.cell_at((3, 2)))
        self.assertEqual(8, down.cell_at((3, 1)))
        self.assertEqual(16, down.cell_at((3, 0)))
        for row in range(3):
            for col in range(4):
                self.assertEqual(0, down.cell_at((row, col)))

    def testShiftTakenSpaces(self):
        state = NumbersState.from_table(
            [[4, 0, 0, 2],
             [0, 0, 4, 8],
             [0, 8, 2, 0],
             [16, 2, 0, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(2, right.cell_at((0, 3)))
        self.assertEqual(8, right.cell_at((1, 3)))
        self.assertEqual(2, right.cell_at((2, 3)))
        self.assertEqual(2, right.cell_at((3, 3)))
        self.assertEqual(4, right.cell_at((0, 2)))
        self.assertEqual(4, right.cell_at((1, 2)))
        self.assertEqual(8, right.cell_at((2, 2)))
        self.assertEqual(16, right.cell_at((3, 2)))
        for row in range(4):
            for col in range(2):
                self.assertEqual(0, right.cell_at((row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(4, left.cell_at((0, 0)))
        self.assertEqual(4, left.cell_at((1, 0)))
        self.assertEqual(8, left.cell_at((2, 0)))
        self.assertEqual(16, left.cell_at((3, 0)))
        self.assertEqual(2, left.cell_at((0, 1)))
        self.assertEqual(8, left.cell_at((1, 1)))
        self.assertEqual(2, left.cell_at((2, 1)))
        self.assertEqual(2, left.cell_at((3, 1)))
        for row in range(4):
            for col in range(2, 4):
                self.assertEqual(0, left.cell_at((row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(2, up.cell_at((0, 3)))
        self.assertEqual(4, up.cell_at((0, 2)))
        self.assertEqual(8, up.cell_at((0, 1)))
        self.assertEqual(4, up.cell_at((0, 0)))
        self.assertEqual(8, up.cell_at((1, 3)))
        self.assertEqual(2, up.cell_at((1, 2)))
        self.assertEqual(2, up.cell_at((1, 1)))
        self.assertEqual(16, up.cell_at((1, 0)))
        for row in range(2, 4):
            for col in range(4):
                self.assertEqual(0, up.cell_at((row, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(8, down.cell_at((3, 3)))
        self.assertEqual(2, down.cell_at((3, 2)))
        self.assertEqual(2, down.cell_at((3, 1)))
        self.assertEqual(16, down.cell_at((3, 0)))
        self.assertEqual(2, down.cell_at((2, 3)))
        self.assertEqual(4, down.cell_at((2, 2)))
        self.assertEqual(8, down.cell_at((2, 1)))
        self.assertEqual(4, down.cell_at((2, 0)))
        for row in range(2):
            for col in range(4):
                self.assertEqual(0, down.cell_at((row, col)))

    def testSimpleSums(self):
        state = NumbersState.from_table(
            [[2, 0, 0, 2],
             [0, 0, 2, 2],
             [0, 2, 2, 0],
             [2, 2, 0, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(4, right.cell_at((0, 3)))
        self.assertEqual(4, right.cell_at((1, 3)))
        self.assertEqual(4, right.cell_at((2, 3)))
        self.assertEqual(4, right.cell_at((3, 3)))
        for row in range(4):
            for col in range(3):
                self.assertEqual(0, right.cell_at((row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(4, left.cell_at((0, 0)))
        self.assertEqual(4, left.cell_at((1, 0)))
        self.assertEqual(4, left.cell_at((2, 0)))
        self.assertEqual(4, left.cell_at((3, 0)))
        for row in range(4):
            for col in range(1, 4):
                self.assertEqual(0, left.cell_at((row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(4, up.cell_at((0, 3)))
        self.assertEqual(4, up.cell_at((0, 2)))
        self.assertEqual(4, up.cell_at((0, 1)))
        self.assertEqual(4, up.cell_at((0, 0)))
        for row in range(1, 4):
            for col in range(4):
                self.assertEqual(0, up.cell_at((row, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(4, down.cell_at((3, 3)))
        self.assertEqual(4, down.cell_at((3, 2)))
        self.assertEqual(4, down.cell_at((3, 1)))
        self.assertEqual(4, down.cell_at((3, 0)))
        for row in range(3):
            for col in range(4):
                self.assertEqual(0, down.cell_at((row, col)))

    def testComplexSums(self):
        state = NumbersState.from_table(
            [[2, 2, 2, 2],
             [4, 0, 2, 2],
             [0, 8, 0, 2],
             [2, 2, 4, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(4, right.cell_at((0, 3)), '\n' + str(right))
        self.assertEqual(4, right.cell_at((1, 3)))
        self.assertEqual(2, right.cell_at((2, 3)))
        self.assertEqual(4, right.cell_at((3, 3)), '\n' + str(right))
        self.assertEqual(4, right.cell_at((0, 2)))
        self.assertEqual(4, right.cell_at((1, 2)))
        self.assertEqual(8, right.cell_at((2, 2)))
        self.assertEqual(4, right.cell_at((3, 2)))
        for row in range(4):
            for col in range(2):
                self.assertEqual(0, right.cell_at((row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(4, left.cell_at((0, 0)))
        self.assertEqual(4, left.cell_at((1, 0)))
        self.assertEqual(8, left.cell_at((2, 0)))
        self.assertEqual(4, left.cell_at((3, 0)))
        self.assertEqual(4, left.cell_at((0, 1)))
        self.assertEqual(4, left.cell_at((1, 1)))
        self.assertEqual(2, left.cell_at((2, 1)))
        self.assertEqual(4, left.cell_at((3, 1)))
        for row in range(4):
            for col in range(2, 4):
                self.assertEqual(0, left.cell_at((row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(4, up.cell_at((0, 3)))
        self.assertEqual(4, up.cell_at((0, 2)))
        self.assertEqual(2, up.cell_at((0, 1)))
        self.assertEqual(2, up.cell_at((0, 0)))
        self.assertEqual(2, up.cell_at((1, 3)))
        self.assertEqual(4, up.cell_at((1, 2)))
        self.assertEqual(8, up.cell_at((1, 1)))
        self.assertEqual(4, up.cell_at((1, 0)))
        self.assertEqual(0, up.cell_at((2, 3)))
        self.assertEqual(0, up.cell_at((2, 2)))
        self.assertEqual(2, up.cell_at((2, 1)))
        self.assertEqual(2, up.cell_at((2, 0)))
        for col in range(4):
            self.assertEqual(0, up.cell_at((3, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(4, down.cell_at((3, 3)))
        self.assertEqual(4, down.cell_at((3, 2)))
        self.assertEqual(2, down.cell_at((3, 1)))
        self.assertEqual(2, down.cell_at((3, 0)))
        self.assertEqual(2, down.cell_at((2, 3)))
        self.assertEqual(4, down.cell_at((2, 2)))
        self.assertEqual(8, down.cell_at((2, 1)))
        self.assertEqual(4, down.cell_at((2, 0)))
        self.assertEqual(0, down.cell_at((1, 3)))
        self.assertEqual(0, down.cell_at((1, 2)))
        self.assertEqual(2, down.cell_at((1, 1)))
        self.assertEqual(2, down.cell_at((1, 0)))
        for col in range(4):
            self.assertEqual(0, down.cell_at((0, col)))

    def test_no_successors_for_no_moves(self):
        state = NumbersState.from_table(
            [[0, 0, 0, 2],
             [0, 0, 0, 4],
             [0, 0, 0, 8],
             [0, 0, 0, 16]])

        self.assertFalse(RIGHT in state.get_successors())

        left = state.get_successors()[LEFT]
        self.assertEqual(2, left.cell_at((0, 0)))
        self.assertEqual(4, left.cell_at((1, 0)))
        self.assertEqual(8, left.cell_at((2, 0)))
        self.assertEqual(16, left.cell_at((3, 0)))
        for row in range(4):
            for col in range(1, 4):
                self.assertEqual(0, left.cell_at((row, col)))

        self.assertFalse(UP in state.get_successors())

        self.assertFalse(DOWN in state.get_successors())


if __name__ == "__main__":
    unittest.main()
