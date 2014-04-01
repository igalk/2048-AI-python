from search.algorithm import Heuristic


class BasicHeuristic(Heuristic):
    def evaluate(self, state):
        score = 0
        for x in xrange(4):
            for y in xrange(4):
                cell = state.cell_at((y, x))
                if cell > 0:
                    score += (cell / 2 - 1)
                else:
                    score += 32

                # Boost if has equal adjacent cells
                if x > 0 and cell == state.cell_at((x-1, y)):
                    score += 1
                if y > 0 and cell == state.cell_at((x, y-1)):
                    score += 1

        return score
