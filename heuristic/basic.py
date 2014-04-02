import math
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

                    # Boost if has equal adjacent cells
                    if x > 0 and cell == state.cell_at((y, x-1)):
                        adjacent += 1
                    if y > 0 and cell == state.cell_at((y-1, x)):
                        adjacent += 1
                else:
                    empty += 1
                snakes.append(BasicHeuristic.snake_rec(x, y, cell, state))

        monotonic_up = 0
        monotonic_down = 0
        monotonic_left = 0
        monotonic_right = 0
        for x in xrange(4):
            current = 0
            next = current + 1
            while next < 4:
                while next < 3 and not state.cell_at((next, x)):
                    next += 1
                current_cell = state.cell_at((current, x))
                current_value = math.log(current_cell, 2) if current_cell else 0
                next_cell = state.cell_at((next, x))
                next_value = math.log(next_cell, 2) if next_cell else 0
                if current_value > next_value:
                    monotonic_up += (next_value - current_value)
                elif next_value > current_value:
                    monotonic_down += (current_value - next_value)
                current = next
                next += 1
        for y in xrange(4):
            current = 0
            next = current + 1
            while next < 4:
                while next < 3 and not state.cell_at((y, next)):
                    next += 1
                current_cell = state.cell_at((y, current))
                current_value = math.log(current_cell, 2) if current_cell else 0
                next_cell = state.cell_at((y, next))
                next_value = math.log(next_cell, 2) if next_cell else 0
                if current_value > next_value:
                    monotonic_left += (next_value - current_value)
                elif next_value > current_value:
                    monotonic_right += (current_value - next_value)
                current = next
                next += 1
        monotonic = max(monotonic_up, monotonic_down) + max(monotonic_left, monotonic_right)

        # print "cell_score: %d" % cell_score
        # print "empty: %d" % empty
        # print "adjacent: %d" % adjacent
        # print "snakes: %s" % snakes
        # print "monotonic: %d" % monotonic

        return cell_score + empty*32 + adjacent*4 + max(snakes)*9 + monotonic

    @staticmethod
    def snake_rec(x, y, tile, state):
        snakes = [0]
        if x > 0:
            cell = state.cell_at((y, x-1))
            if (tile and tile*2 == cell) or (tile == 0 and cell == 2):
                snakes.append(1 + BasicHeuristic.snake_rec(x-1, y, cell, state))
        if x < 3:
            cell = state.cell_at((y, x+1))
            if (tile and tile*2 == cell) or (tile == 0 and cell == 2):
                snakes.append(1 + BasicHeuristic.snake_rec(x+1, y, cell, state))
        if y > 0:
            cell = state.cell_at((y-1, x))
            if (tile and tile*2 == cell) or (tile == 0 and cell == 2):
                snakes.append(1 + BasicHeuristic.snake_rec(x, y-1, cell, state))
        if y < 3:
            cell = state.cell_at((y+1, x))
            if (tile and tile*2 == cell) or (tile == 0 and cell == 2):
                snakes.append(1 + BasicHeuristic.snake_rec(x, y+1, cell, state))
        return max(snakes)
