import unittest

from numbers_problem2 import *


class NumbersState2Test(unittest.TestCase):
    def test_shift_empty_spaces(self):
        state = NumbersState2.from_table(
            [[0, 0, 0, 2],
             [0, 0, 4, 0],
             [0, 8, 0, 0],
             [16, 0, 0, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(2, right.cell_at(Index(0, 3)).value)
        self.assertEqual(4, right.cell_at(Index(1, 3)).value)
        self.assertEqual(8, right.cell_at(Index(2, 3)).value)
        self.assertEqual(16, right.cell_at(Index(3, 3)).value)
        for row in range(4):
            for col in range(3):
                self.assertIsNone(right.cell_at(Index(row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(2, left.cell_at(Index(0, 0)).value)
        self.assertEqual(4, left.cell_at(Index(1, 0)).value)
        self.assertEqual(8, left.cell_at(Index(2, 0)).value)
        self.assertEqual(16, left.cell_at(Index(3, 0)).value)
        for row in range(4):
            for col in range(1, 4):
                self.assertIsNone(left.cell_at(Index(row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(2, up.cell_at(Index(0, 3)).value)
        self.assertEqual(4, up.cell_at(Index(0, 2)).value)
        self.assertEqual(8, up.cell_at(Index(0, 1)).value)
        self.assertEqual(16, up.cell_at(Index(0, 0)).value)
        for row in range(1, 4):
            for col in range(4):
                self.assertIsNone(up.cell_at(Index(row, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(2, down.cell_at(Index(3, 3)).value)
        self.assertEqual(4, down.cell_at(Index(3, 2)).value)
        self.assertEqual(8, down.cell_at(Index(3, 1)).value)
        self.assertEqual(16, down.cell_at(Index(3, 0)).value)
        for row in range(3):
            for col in range(4):
                self.assertIsNone(down.cell_at(Index(row, col)))

    def test_shift_taken_spaces(self):
        state = NumbersState2.from_table(
            [[4, 0, 0, 2],
             [0, 0, 4, 8],
             [0, 8, 2, 0],
             [16, 2, 0, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(2, right.cell_at(Index(0, 3)).value)
        self.assertEqual(8, right.cell_at(Index(1, 3)).value)
        self.assertEqual(2, right.cell_at(Index(2, 3)).value)
        self.assertEqual(2, right.cell_at(Index(3, 3)).value)
        self.assertEqual(4, right.cell_at(Index(0, 2)).value)
        self.assertEqual(4, right.cell_at(Index(1, 2)).value)
        self.assertEqual(8, right.cell_at(Index(2, 2)).value)
        self.assertEqual(16, right.cell_at(Index(3, 2)).value)
        for row in range(4):
            for col in range(2):
                self.assertIsNone(right.cell_at(Index(row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(4, left.cell_at(Index(0, 0)).value)
        self.assertEqual(4, left.cell_at(Index(1, 0)).value)
        self.assertEqual(8, left.cell_at(Index(2, 0)).value)
        self.assertEqual(16, left.cell_at(Index(3, 0)).value)
        self.assertEqual(2, left.cell_at(Index(0, 1)).value)
        self.assertEqual(8, left.cell_at(Index(1, 1)).value)
        self.assertEqual(2, left.cell_at(Index(2, 1)).value)
        self.assertEqual(2, left.cell_at(Index(3, 1)).value)
        for row in range(4):
            for col in range(2, 4):
                self.assertIsNone(left.cell_at(Index(row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(2, up.cell_at(Index(0, 3)).value)
        self.assertEqual(4, up.cell_at(Index(0, 2)).value)
        self.assertEqual(8, up.cell_at(Index(0, 1)).value)
        self.assertEqual(4, up.cell_at(Index(0, 0)).value)
        self.assertEqual(8, up.cell_at(Index(1, 3)).value)
        self.assertEqual(2, up.cell_at(Index(1, 2)).value)
        self.assertEqual(2, up.cell_at(Index(1, 1)).value)
        self.assertEqual(16, up.cell_at(Index(1, 0)).value)
        for row in range(2, 4):
            for col in range(4):
                self.assertIsNone(up.cell_at(Index(row, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(8, down.cell_at(Index(3, 3)).value)
        self.assertEqual(2, down.cell_at(Index(3, 2)).value)
        self.assertEqual(2, down.cell_at(Index(3, 1)).value)
        self.assertEqual(16, down.cell_at(Index(3, 0)).value)
        self.assertEqual(2, down.cell_at(Index(2, 3)).value)
        self.assertEqual(4, down.cell_at(Index(2, 2)).value)
        self.assertEqual(8, down.cell_at(Index(2, 1)).value)
        self.assertEqual(4, down.cell_at(Index(2, 0)).value)
        for row in range(2):
            for col in range(4):
                self.assertIsNone(down.cell_at(Index(row, col)))

    def test_simple_merges(self):
        state = NumbersState2.from_table(
            [[2, 0, 0, 2],
             [0, 0, 2, 2],
             [0, 2, 2, 0],
             [2, 2, 0, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(4, right.cell_at(Index(0, 3)).value)
        self.assertEqual(4, right.cell_at(Index(1, 3)).value)
        self.assertEqual(4, right.cell_at(Index(2, 3)).value)
        self.assertEqual(4, right.cell_at(Index(3, 3)).value)
        for row in range(4):
            for col in range(3):
                self.assertIsNone(right.cell_at(Index(row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(4, left.cell_at(Index(0, 0)).value)
        self.assertEqual(4, left.cell_at(Index(1, 0)).value)
        self.assertEqual(4, left.cell_at(Index(2, 0)).value)
        self.assertEqual(4, left.cell_at(Index(3, 0)).value)
        for row in range(4):
            for col in range(1, 4):
                self.assertIsNone(left.cell_at(Index(row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(4, up.cell_at(Index(0, 3)).value)
        self.assertEqual(4, up.cell_at(Index(0, 2)).value)
        self.assertEqual(4, up.cell_at(Index(0, 1)).value)
        self.assertEqual(4, up.cell_at(Index(0, 0)).value)
        for row in range(1, 4):
            for col in range(4):
                self.assertIsNone(up.cell_at(Index(row, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(4, down.cell_at(Index(3, 3)).value)
        self.assertEqual(4, down.cell_at(Index(3, 2)).value)
        self.assertEqual(4, down.cell_at(Index(3, 1)).value)
        self.assertEqual(4, down.cell_at(Index(3, 0)).value)
        for row in range(3):
            for col in range(4):
                self.assertIsNone(down.cell_at(Index(row, col)))

    def test_complex_merges(self):
        state = NumbersState2.from_table(
            [[2, 2, 2, 2],
             [4, 0, 2, 2],
             [0, 8, 0, 2],
             [2, 2, 4, 0]])

        right = state.get_successors()[RIGHT]
        self.assertEqual(4, right.cell_at(Index(0, 3)).value)
        self.assertEqual(4, right.cell_at(Index(1, 3)).value)
        self.assertEqual(2, right.cell_at(Index(2, 3)).value)
        self.assertEqual(4, right.cell_at(Index(3, 3)).value)
        self.assertEqual(4, right.cell_at(Index(0, 2)).value)
        self.assertEqual(4, right.cell_at(Index(1, 2)).value)
        self.assertEqual(8, right.cell_at(Index(2, 2)).value)
        self.assertEqual(4, right.cell_at(Index(3, 2)).value)
        for row in range(4):
            for col in range(2):
                self.assertIsNone(right.cell_at(Index(row, col)))

        left = state.get_successors()[LEFT]
        self.assertEqual(4, left.cell_at(Index(0, 0)).value)
        self.assertEqual(4, left.cell_at(Index(1, 0)).value)
        self.assertEqual(8, left.cell_at(Index(2, 0)).value)
        self.assertEqual(4, left.cell_at(Index(3, 0)).value)
        self.assertEqual(4, left.cell_at(Index(0, 1)).value)
        self.assertEqual(4, left.cell_at(Index(1, 1)).value)
        self.assertEqual(2, left.cell_at(Index(2, 1)).value)
        self.assertEqual(4, left.cell_at(Index(3, 1)).value)
        for row in range(4):
            for col in range(2, 4):
                self.assertIsNone(left.cell_at(Index(row, col)))

        up = state.get_successors()[UP]
        self.assertEqual(4, up.cell_at(Index(0, 3)).value)
        self.assertEqual(4, up.cell_at(Index(0, 2)).value)
        self.assertEqual(2, up.cell_at(Index(0, 1)).value)
        self.assertEqual(2, up.cell_at(Index(0, 0)).value)
        self.assertEqual(2, up.cell_at(Index(1, 3)).value)
        self.assertEqual(4, up.cell_at(Index(1, 2)).value)
        self.assertEqual(8, up.cell_at(Index(1, 1)).value)
        self.assertEqual(4, up.cell_at(Index(1, 0)).value)
        self.assertIsNone(up.cell_at(Index(2, 3)))
        self.assertIsNone(up.cell_at(Index(2, 2)))
        self.assertEqual(2, up.cell_at(Index(2, 1)).value)
        self.assertEqual(2, up.cell_at(Index(2, 0)).value)
        for col in range(4):
            self.assertIsNone(up.cell_at(Index(3, col)))

        down = state.get_successors()[DOWN]
        self.assertEqual(4, down.cell_at(Index(3, 3)).value)
        self.assertEqual(4, down.cell_at(Index(3, 2)).value)
        self.assertEqual(2, down.cell_at(Index(3, 1)).value)
        self.assertEqual(2, down.cell_at(Index(3, 0)).value)
        self.assertEqual(2, down.cell_at(Index(2, 3)).value)
        self.assertEqual(4, down.cell_at(Index(2, 2)).value)
        self.assertEqual(8, down.cell_at(Index(2, 1)).value)
        self.assertEqual(4, down.cell_at(Index(2, 0)).value)
        self.assertIsNone(down.cell_at(Index(1, 3)))
        self.assertIsNone(down.cell_at(Index(1, 2)))
        self.assertEqual(2, down.cell_at(Index(1, 1)).value)
        self.assertEqual(2, down.cell_at(Index(1, 0)).value)
        for col in range(4):
            self.assertIsNone(down.cell_at(Index(0, col)))

    def test_no_successors_for_no_moves(self):
        state = NumbersState2.from_table(
            [[0, 0, 0, 2],
             [0, 0, 0, 4],
             [0, 0, 0, 8],
             [0, 0, 0, 16]])

        self.assertFalse(RIGHT in state.get_successors())

        left = state.get_successors()[LEFT]
        self.assertEqual(2, left.cell_at(Index(0, 0)).value)
        self.assertEqual(4, left.cell_at(Index(1, 0)).value)
        self.assertEqual(8, left.cell_at(Index(2, 0)).value)
        self.assertEqual(16, left.cell_at(Index(3, 0)).value)
        for row in range(4):
            for col in range(1, 4):
                self.assertIsNone(left.cell_at(Index(row, col)))

        self.assertFalse(UP in state.get_successors())

        self.assertFalse(DOWN in state.get_successors())


if __name__ == "__main__":
    unittest.main()
