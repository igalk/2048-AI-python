import unittest

from heuristic.basic2 import BasicHeuristic2
from numbers_problem2 import *


class Heuristic2Test(unittest.TestCase):
    def test_merge_adjacent_cells(self):
        state = NumbersState2.from_table(
            [[2, 4, 8, 16],
             [2, 32, 2, 32],
             [8, 16, 4, 64],
             [16, 2, 128, 4]])

        successors = state.get_successors()
        h = BasicHeuristic2()
        self.assertGreater(h.evaluate(successors[UP]), h.evaluate(successors[DOWN]))


if __name__ == "__main__":
    unittest.main()
