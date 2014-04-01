import math
from random import random, choice
from problem import ProblemState
from direction import *


win_score = 4096


class Index:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def within_bounds(self):
        return 0 <= self.x < 4 and 0 <= self.y < 4

    def __cmp__(self, other):
        return cmp((self.x, self.y), (other.x, other.y))

    def __str__(self):
        return "(%d, %d)" % (self.y, self.x)


class Tile(Index):
    def __init__(self, y, x, value):
        Index.__init__(self, y, x)
        self.value = value or 2
        self.previous_position = None
        self.merged_from = None

    def save_position(self):
        self.previous_position = Index(self.y, self.x)

    def update_position(self, position):
        self.x = position.x
        self.y = position.y

    def clone(self):
        return Tile(self.y, self.x, self.value)

    def __str__(self):
        return "(%d, %d) : %d" % (self.y, self.x, self.value)


class NumbersState2(ProblemState):
    def __init__(self):
        self.cells = [[None] * 4 for _ in xrange(4)]

    def random_available_cell(self):
        cells = self.available_cells()
        if len(cells):
            return random.choice(cells)

    def available_cells(self):
        cells = []

        def f(x, y, tile):
            if not tile:
                cells.append(Index(y, x))

        self.each_cell(f)
        return cells

    def each_cell(self, f):
        for x in xrange(4):
            row = self.cells[x]
            for y in xrange(4):
                f(x, y, row[y])

    def cell_at(self, cell):
        return self.cells[cell.y][cell.x] if cell.within_bounds() else None

    def insert_tile(self, tile):
        self.cells[tile.y][tile.x] = tile

    def remove_tile(self, tile):
        self.cells[tile.y][tile.x] = None

    def clone(self):
        new_state = NumbersState2()

        def f(x, y, tile):
            if tile:
                new_state.insert_tile(tile.clone())

        self.each_cell(f)
        return new_state

    def mutate(self):
        empty = self.available_cells()
        cell = choice(empty)
        value = 2 if random() < 0.9 else 4

        new_state = self.clone()
        tile = Tile(cell.y, cell.x, value)
        new_state.insert_tile(tile)
        return new_state

    def prepare_tiles(self):
        def f(x, y, tile):
            if tile:
                tile.merged_from = None
                tile.save_position()

        self.each_cell(f)

    def move_tile(self, tile, cell):
        self.cells[tile.y][tile.x] = None
        self.cells[cell.y][cell.x] = tile
        tile.update_position(cell)

    def move(self, direction):
        traversals = direction.build_traversals()
        moved = False
        score = 0
        won = False

        # Save the current tile positions and remove merger information
        self.prepare_tiles()

        # Traverse the grid in the right direction and move tiles
        for x in traversals['x']:
            for y in traversals['y']:
                cell = Index(y, x)
                tile = self.cell_at(cell)

                if tile:
                    positions = self.find_farthest_position(cell, direction)
                    next_position = positions['next']
                    next = self.cell_at(next_position)

                    # Only one merger per row traversal?
                    if next and next.value == tile.value and not next.merged_from:
                        merged = Tile(next_position.y, next_position.x, tile.value * 2)
                        merged.merged_from = [tile, next]

                        self.insert_tile(merged)
                        self.remove_tile(tile)

                        # Converge the two tiles' positions
                        tile.update_position(next_position)

                        # Update the score
                        score += merged.value

                        # The mighty win tile
                        if merged.value == win_score:
                            won = True
                    else:
                        self.move_tile(tile, positions['farthest'])

                    if not cell == tile:
                        moved = True

        return {'moved': moved, 'score': score, 'won': won}

    def get_successors(self):
        successors = {}
        for direction in [UP, RIGHT, DOWN, LEFT]:
            new_state = self.clone()
            if new_state.move(direction)['moved']:
                successors[direction] = new_state
        return successors

    def find_farthest_position(self, cell, direction):
        # Progress towards the vector direction until an obstacle is found
        previous = cell
        cell = Index(previous.y + direction.dy, previous.x + direction.dx)
        while cell.within_bounds() and self.cell_at((cell.y, cell.x)) is None:
            previous = cell
            cell = Index(previous.y + direction.dy, previous.x + direction.dx)

        return {'farthest': previous, 'next': cell}

    def is_goal(self):
        for row in self.cells:
            for tile in row:
                if tile and tile.value == win_score:
                    return True
        return False

    def __str__(self):
        """
        The string representation of the state. ASCII art FTW!
        """
        s = ''
        for row in self.cells:
            s += '|'
            for tile in row:
                print_format = "%%%dd|" % round(math.log(win_score, 10) + 0.5)
                s += print_format % (tile.value if tile else 0)
            s += '\n'
        return s

    @staticmethod
    def from_table(table):
        state = NumbersState2()
        for y, row in enumerate(table):
            for x, cell in enumerate(row):
                if cell:
                    state.insert_tile(Tile(y, x, cell))
        return state

    @staticmethod
    def random_start():
        state = NumbersState2()
        state = state.mutate()
        state = state.mutate()
        return state
