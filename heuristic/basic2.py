from numbers_problem2 import Index
from search.algorithm import Heuristic


class BasicHeuristic2(Heuristic):
    def evaluate(self, state):
        score = 0
        for x in xrange(4):
            for y in xrange(4):
                tile = state.cell_at(Index(y, x))
                if tile:
                    score += (tile.value / 2 - 1)

                    # Boost if has equal adjacent cells
                    if x > 0:
                        next = state.cell_at(Index(y, x-1))
                        if next and next.value == tile.value:
                            score += 1
                    if y > 0:
                        next = state.cell_at(Index(y-1, x))
                        if next and next.value == tile.value:
                            score += 1
                else:
                    score += 32

        return score
