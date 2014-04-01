from search.algorithm import Heuristic


class BasicHeuristic(Heuristic):
    def evaluate(self, state):
        cell_score = 0
        empty = 0
        adjacent = 0
        snakes = [1]
        for x in xrange(4):
            for y in xrange(4):
                cell = state.cell_at((y, x))
                if cell > 0:
                    cell_score += (cell / 2 - 1)
                    snakes.append(BasicHeuristic.snake_rec(x, y, cell, state))
                else:
                    empty += 1

                # Boost if has equal adjacent cells
                if x > 0 and cell == state.cell_at((y, x-1)):
                    adjacent += 1
                if y > 0 and cell == state.cell_at((y-1, x)):
                    adjacent += 1

        return cell_score + empty*32 + adjacent + max(snakes)

    @staticmethod
    def snake_rec(x, y, tile, state):
        snakes = [0]
        if x > 0:
            cell = state.cell_at((y, x-1))
            if cell == tile/2:
                snakes.append(1 + BasicHeuristic.snake_rec(x-1, y, cell, state))
        if x < 3:
            cell = state.cell_at((y, x+1))
            if cell == tile/2:
                snakes.append(1 + BasicHeuristic.snake_rec(x+1, y, cell, state))
        if y > 0:
            cell = state.cell_at((y-1, x))
            if cell == tile/2:
                snakes.append(1 + BasicHeuristic.snake_rec(x, y-1, cell, state))
        if y < 3:
            cell = state.cell_at((y+1, x))
            if cell == tile/2:
                snakes.append(1 + BasicHeuristic.snake_rec(x, y+1, cell, state))
        return max(snakes)
