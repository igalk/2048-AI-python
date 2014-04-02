import unittest

from numbers_problem import *
from heuristic.basic import BasicHeuristic


class HeuristicTest(unittest.TestCase):
    def test_merge_adjacent_cells(self):
        state = NumbersState.from_table(
            [[2, 4, 8, 16],
             [2, 32, 2, 32],
             [8, 16, 4, 64],
             [16, 2, 128, 4]])

        successors = state.get_successors()
        h = BasicHeuristic()
        self.assertGreater(h.evaluate(successors[UP]), h.evaluate(successors[DOWN]))

    def test_merge_adjacent_cells2(self):
        state = NumbersState.from_table(
            [[2, 8, 32, 2],
             [0, 16, 64, 8],
             [2, 32, 256, 16],
             [4, 2, 32, 8]])

        successors = state.get_successors()
        h = BasicHeuristic()
        self.assertGreater(h.evaluate(successors[UP]), h.evaluate(successors[DOWN]))

    def test_merge_adjacent_cells3(self):
        state = NumbersState.from_table(
            [[16, 4, 8, 32],
             [4, 512, 16, 128],
             [32, 8, 32, 2],
             [2, 4, 4, 2]])

        successors = state.get_successors()
        h = BasicHeuristic()
        self.assertGreater(h.evaluate(successors[DOWN]), h.evaluate(successors[UP]))

    def test_snake_with_empty_space(self):
        state = NumbersState.from_table(
            [[4, 32, 4, 0],
             [2, 4, 4, 4],
             [4, 64, 32, 128],
             [0, 0, 0, 0]])

        successors = state.get_successors()
        h = BasicHeuristic()
        self.assertGreater(h.evaluate(successors[RIGHT]), h.evaluate(successors[DOWN]))


if __name__ == "__main__":
    unittest.main()
