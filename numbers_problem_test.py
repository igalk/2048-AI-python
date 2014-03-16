import unittest
from numbers_problem import *

class Test(unittest.TestCase):
    def testShiftEmptySpaces(self):
        state = NumbersState.fromTable(
            [[ 0, 0, 0, 2],
             [ 0, 0, 4, 0],
             [ 0, 8, 0, 0],
             [16, 0, 0, 0]])

        right = state.getSuccessors()[RIGHT]
        self.assertEqual( 2, right.cellAt((0, 3)))
        self.assertEqual( 4, right.cellAt((1, 3)))
        self.assertEqual( 8, right.cellAt((2, 3)))
        self.assertEqual(16, right.cellAt((3, 3)))
        for row in range(4):
            for col in range(3):
                self.assertEqual(0, right.cellAt((row, col)))

        left = state.getSuccessors()[LEFT]
        self.assertEqual( 2, left.cellAt((0, 0)))
        self.assertEqual( 4, left.cellAt((1, 0)))
        self.assertEqual( 8, left.cellAt((2, 0)))
        self.assertEqual(16, left.cellAt((3, 0)))
        for row in range(4):
            for col in range(1, 4):
                self.assertEqual(0, left.cellAt((row, col)))

        up = state.getSuccessors()[UP]
        self.assertEqual( 2, up.cellAt((0, 3)))
        self.assertEqual( 4, up.cellAt((0, 2)))
        self.assertEqual( 8, up.cellAt((0, 1)))
        self.assertEqual(16, up.cellAt((0, 0)))
        for row in range(1, 4):
            for col in range(4):
                self.assertEqual(0, up.cellAt((row, col)))

        down = state.getSuccessors()[DOWN]
        self.assertEqual( 2, down.cellAt((3, 3)))
        self.assertEqual( 4, down.cellAt((3, 2)))
        self.assertEqual( 8, down.cellAt((3, 1)))
        self.assertEqual(16, down.cellAt((3, 0)))
        for row in range(3):
            for col in range(4):
                self.assertEqual(0, down.cellAt((row, col)))

    def testShiftTakenSpaces(self):
        state = NumbersState.fromTable(
            [[ 4, 0, 0, 2],
             [ 0, 0, 4, 8],
             [ 0, 8, 2, 0],
             [16, 2, 0, 0]])

        right = state.getSuccessors()[RIGHT]
        self.assertEqual( 2, right.cellAt((0, 3)))
        self.assertEqual( 8, right.cellAt((1, 3)))
        self.assertEqual( 2, right.cellAt((2, 3)))
        self.assertEqual( 2, right.cellAt((3, 3)))
        self.assertEqual( 4, right.cellAt((0, 2)))
        self.assertEqual( 4, right.cellAt((1, 2)))
        self.assertEqual( 8, right.cellAt((2, 2)))
        self.assertEqual(16, right.cellAt((3, 2)))
        for row in range(4):
            for col in range(2):
                self.assertEqual(0, right.cellAt((row, col)))

        left = state.getSuccessors()[LEFT]
        self.assertEqual( 4, left.cellAt((0, 0)))
        self.assertEqual( 4, left.cellAt((1, 0)))
        self.assertEqual( 8, left.cellAt((2, 0)))
        self.assertEqual(16, left.cellAt((3, 0)))
        self.assertEqual( 2, left.cellAt((0, 1)))
        self.assertEqual( 8, left.cellAt((1, 1)))
        self.assertEqual( 2, left.cellAt((2, 1)))
        self.assertEqual( 2, left.cellAt((3, 1)))
        for row in range(4):
            for col in range(2, 4):
                self.assertEqual(0, left.cellAt((row, col)))

        up = state.getSuccessors()[UP]
        self.assertEqual( 2, up.cellAt((0, 3)))
        self.assertEqual( 4, up.cellAt((0, 2)))
        self.assertEqual( 8, up.cellAt((0, 1)))
        self.assertEqual( 4, up.cellAt((0, 0)))
        self.assertEqual( 8, up.cellAt((1, 3)))
        self.assertEqual( 2, up.cellAt((1, 2)))
        self.assertEqual( 2, up.cellAt((1, 1)))
        self.assertEqual(16, up.cellAt((1, 0)))
        for row in range(2, 4):
            for col in range(4):
                self.assertEqual(0, up.cellAt((row, col)))

        down = state.getSuccessors()[DOWN]
        self.assertEqual( 8, down.cellAt((3, 3)))
        self.assertEqual( 2, down.cellAt((3, 2)))
        self.assertEqual( 2, down.cellAt((3, 1)))
        self.assertEqual(16, down.cellAt((3, 0)))
        self.assertEqual( 2, down.cellAt((2, 3)))
        self.assertEqual( 4, down.cellAt((2, 2)))
        self.assertEqual( 8, down.cellAt((2, 1)))
        self.assertEqual( 4, down.cellAt((2, 0)))
        for row in range(2):
            for col in range(4):
                self.assertEqual(0, down.cellAt((row, col)))

    def testSimpleSums(self):
        state = NumbersState.fromTable(
            [[2, 0, 0, 2],
             [0, 0, 2, 2],
             [0, 2, 2, 0],
             [2, 2, 0, 0]])

        right = state.getSuccessors()[RIGHT]
        self.assertEqual(4, right.cellAt((0, 3)))
        self.assertEqual(4, right.cellAt((1, 3)))
        self.assertEqual(4, right.cellAt((2, 3)))
        self.assertEqual(4, right.cellAt((3, 3)))
        for row in range(4):
            for col in range(3):
                self.assertEqual(0, right.cellAt((row, col)))

        left = state.getSuccessors()[LEFT]
        self.assertEqual(4, left.cellAt((0, 0)))
        self.assertEqual(4, left.cellAt((1, 0)))
        self.assertEqual(4, left.cellAt((2, 0)))
        self.assertEqual(4, left.cellAt((3, 0)))
        for row in range(4):
            for col in range(1, 4):
                self.assertEqual(0, left.cellAt((row, col)))

        up = state.getSuccessors()[UP]
        self.assertEqual(4, up.cellAt((0, 3)))
        self.assertEqual(4, up.cellAt((0, 2)))
        self.assertEqual(4, up.cellAt((0, 1)))
        self.assertEqual(4, up.cellAt((0, 0)))
        for row in range(1, 4):
            for col in range(4):
                self.assertEqual(0, up.cellAt((row, col)))

        down = state.getSuccessors()[DOWN]
        self.assertEqual(4, down.cellAt((3, 3)))
        self.assertEqual(4, down.cellAt((3, 2)))
        self.assertEqual(4, down.cellAt((3, 1)))
        self.assertEqual(4, down.cellAt((3, 0)))
        for row in range(3):
            for col in range(4):
                self.assertEqual(0, down.cellAt((row, col)))

    def testComplexSums(self):
        state = NumbersState.fromTable(
            [[2, 2, 2, 2],
             [4, 0, 2, 2],
             [0, 8, 0, 2],
             [2, 2, 4, 0]])

        right = state.getSuccessors()[RIGHT]
        self.assertEqual(4, right.cellAt((0, 3)), '\n'+str(right))
        self.assertEqual(4, right.cellAt((1, 3)))
        self.assertEqual(2, right.cellAt((2, 3)))
        self.assertEqual(4, right.cellAt((3, 3)), '\n'+str(right))
        self.assertEqual(4, right.cellAt((0, 2)))
        self.assertEqual(4, right.cellAt((1, 2)))
        self.assertEqual(8, right.cellAt((2, 2)))
        self.assertEqual(4, right.cellAt((3, 2)))
        for row in range(4):
            for col in range(2):
                self.assertEqual(0, right.cellAt((row, col)))

        left = state.getSuccessors()[LEFT]
        self.assertEqual(4, left.cellAt((0, 0)))
        self.assertEqual(4, left.cellAt((1, 0)))
        self.assertEqual(8, left.cellAt((2, 0)))
        self.assertEqual(4, left.cellAt((3, 0)))
        self.assertEqual(4, left.cellAt((0, 1)))
        self.assertEqual(4, left.cellAt((1, 1)))
        self.assertEqual(2, left.cellAt((2, 1)))
        self.assertEqual(4, left.cellAt((3, 1)))
        for row in range(4):
            for col in range(2, 4):
                self.assertEqual(0, left.cellAt((row, col)))

        up = state.getSuccessors()[UP]
        self.assertEqual(4, up.cellAt((0, 3)))
        self.assertEqual(4, up.cellAt((0, 2)))
        self.assertEqual(2, up.cellAt((0, 1)))
        self.assertEqual(2, up.cellAt((0, 0)))
        self.assertEqual(2, up.cellAt((1, 3)))
        self.assertEqual(4, up.cellAt((1, 2)))
        self.assertEqual(8, up.cellAt((1, 1)))
        self.assertEqual(4, up.cellAt((1, 0)))
        self.assertEqual(0, up.cellAt((2, 3)))
        self.assertEqual(0, up.cellAt((2, 2)))
        self.assertEqual(2, up.cellAt((2, 1)))
        self.assertEqual(2, up.cellAt((2, 0)))
        for col in range(4):
            self.assertEqual(0, up.cellAt((3, col)))

        down = state.getSuccessors()[DOWN]
        self.assertEqual(4, down.cellAt((3, 3)))
        self.assertEqual(4, down.cellAt((3, 2)))
        self.assertEqual(2, down.cellAt((3, 1)))
        self.assertEqual(2, down.cellAt((3, 0)))
        self.assertEqual(2, down.cellAt((2, 3)))
        self.assertEqual(4, down.cellAt((2, 2)))
        self.assertEqual(8, down.cellAt((2, 1)))
        self.assertEqual(4, down.cellAt((2, 0)))
        self.assertEqual(0, down.cellAt((1, 3)))
        self.assertEqual(0, down.cellAt((1, 2)))
        self.assertEqual(2, down.cellAt((1, 1)))
        self.assertEqual(2, down.cellAt((1, 0)))
        for col in range(4):
            self.assertEqual(0, down.cellAt((0, col)))

if __name__ == "__main__":
  unittest.main()
