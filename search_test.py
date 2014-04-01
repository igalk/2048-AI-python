import unittest
from basic_agent import BasicAgent
from numbers_problem import *
from heuristic.basic import BasicHeuristic


class SearchTest(unittest.TestCase):
    def test_merge_adjacent_cells(self):
        state = NumbersState.from_table(
            [[2, 8, 32, 2],
             [0, 16, 64, 8],
             [2, 32, 256, 16],
             [4, 2, 32, 8]])

        agent = BasicAgent(BasicHeuristic())
        self.assertEqual(UP, agent.solve(state, 1))
        # successors = state.get_successors()
        # h = BasicHeuristic()
        # for direction, s in successors.iteritems():
        #     print direction
        #     print s
        #     print s.score()
        #     print h.evaluate(s)


if __name__ == "__main__":
    unittest.main()
