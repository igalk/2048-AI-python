from problem import ProblemState, ProblemAction
from math import *
from random import randint

BOARD_SIZE = 4 #cells
CELL_SIZE = 12 #bits
GOAL = (1<<(CELL_SIZE-1))
ALL_ONES = ((GOAL<<1)-1)

FULL_BOARD = 0
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        FULL_BOARD |= (ALL_ONES<<((row*BOARD_SIZE+col)*CELL_SIZE))

class NumbersState(ProblemState):
    '''
    A Numbers state.
    
    Contains:
    - the current state of the board.
    
    Note that this class is immutable.
    '''
    
    def __init__(self, board):
        '''
        Creates a new Numbers state.
        @param board: The current state of the board.
        '''
        self.board = board
    
    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly 
        positive if self > other.
        '''
        return cmp(self.board, other.board)
    
    def __hash__(self):
        '''
        The hash method must be implemented for states to be inserted into sets 
        and dictionaries.
        @return: The hash value of the state.
        '''
        return hash(self.board)
    
    def __str__(self):
        '''
        The string representation of the state. ASCII art FTW!
        '''
        b = self.board
        s = ''
        for y in range(BOARD_SIZE):
            s += '|'
            for x in range(BOARD_SIZE):
                format = "%%%dd|" % round(log(GOAL,10)+0.5)
                s += format % (b&ALL_ONES)
                b = (b>>CELL_SIZE)
            s += '\n'        
        return s
    
    def getSuccessors(self):
        '''
        Generates all the actions that can be performed from this state, and
        the states those actions will create.
        
        @return: A dictionary containing each action as a key, and it's state.
        '''
        successors = {}
        
        for direction in (RIGHT, LEFT, UP, DOWN):
            new_state = NumbersState(self.board)
            successors[direction] = new_state
            merged = []
            if direction == RIGHT:
                for row in range(BOARD_SIZE):
                    for i in range(BOARD_SIZE-2, -1, -1):
                        for col in range(i, BOARD_SIZE-1, 1):
                            self._moveCell(row, col, direction, new_state, merged)
            elif direction == LEFT:
                for row in range(BOARD_SIZE):
                    for i in range(1, BOARD_SIZE, 1):
                        for col in range(i, 0, -1):
                            self._moveCell(row, col, direction, new_state, merged)
            elif direction == UP:
                for col in range(BOARD_SIZE):
                    for i in range(1, BOARD_SIZE, 1):
                        for row in range(i, 0, -1):
                            self._moveCell(row, col, direction, new_state, merged)
            elif direction == DOWN:
                for col in range(BOARD_SIZE):
                    for i in range(BOARD_SIZE-2, -1, -1):
                        for row in range(i, BOARD_SIZE-1, 1):
                            self._moveCell(row, col, direction, new_state, merged)

        return successors

    def getMutations(self):
        empty = []
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.cellAt((y, x)) == 0:
                    empty.append((y, x))
        mutations = {}
        for p in empty:
            new_state = NumbersState(self.board)
            new_state.setCell(p, 2)
            mutations[new_state] = ((4.0/5)/len(empty))
            new_state = NumbersState(self.board)
            new_state.setCell(p, 4)
            mutations[new_state] = ((1.0/5)/len(empty))
        return mutations
    
    def _moveCell(self, row, col, direction, new_state, merged):
        place = (row, col)
        new_place = (row+direction.dy, col+direction.dx)
        cell = new_state.cellAt(place)
        next_cell = new_state.cellAt(new_place)
        if next_cell == 0:
            new_state.setCell(new_place, cell)
            new_state.setCell(place, 0)
            if place in merged:
                merged.remove(place)
                merged.append(new_place)
        elif (next_cell == cell) and (place not in merged) and (new_place not in merged):
            new_state.setCell(new_place, cell<<1)
            new_state.setCell(place, 0)
            merged.append(new_place)

    def cellAt(self, cell):
        return ((self.board>>((cell[0]*BOARD_SIZE+cell[1])*CELL_SIZE))&ALL_ONES)

    def setCell(self, cell, value):
        shift = ((cell[0]*BOARD_SIZE+cell[1])*CELL_SIZE)
        without = FULL_BOARD^(ALL_ONES<<shift)
        self.board = (self.board&without)|(value<<shift)

    def isGoal(self):
        '''
        @return: Whether a 2048 cell exists.
        '''
        # return len([n for n in sum(self.board) if n == GOAL]
        b = self.board
        while b > 0:
            if (b&GOAL):
                return True
            b = (b>>CELL_SIZE)
        return False

    @staticmethod
    def fromTable(table):
        state = NumbersState(0)
        for y, row in enumerate(table):
            for x, cell in enumerate(row):
                state.board |= (cell<<((y*BOARD_SIZE+x)*CELL_SIZE))
        return state

    @staticmethod
    def randomStart():
        state = NumbersState(0)
        for i in range(2):
            cell = randint(0, 16)
            while state.cellAt((cell/BOARD_SIZE, cell%BOARD_SIZE)) != 0:
                cell = randint(0, 16)
            state.setCell((cell/BOARD_SIZE, cell%BOARD_SIZE), 2)
        return state

class MoveAction(ProblemAction):
    '''
    Describes the move in a given direction.
    '''
    
    def __init__(self, direction):
        '''
        Creates a new MoveAction.
        @param direction: A direction to move in.
        '''
        ProblemAction.__init__(self)
        self.direction = direction
    
    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly 
        positive if self > other.
        '''
        return cmp(self.direction, other.direction)
    
    def __hash__(self):
        '''
        The hash method must be implemented for actions to be inserted into sets 
        and dictionaries.
        @return: The hash value of the action.
        '''
        return hash(self.direction)
    
    def __str__(self):
        '''
        @return: The string representation of this object when *str* is called.
        '''
        return str(self.direction)


class Direction():
    '''
    A direction of movement.
    '''
    def __init__(self, name, dy, dx):
        '''
        Creates a new direction.
        @param name: The direction's name.
        '''
        self.name = name
        self.dy = dy
        self.dx = dx
    
    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly 
        positive if self > other.
        '''
        return cmp(self.name, other.name)
    
    def __hash__(self):
        '''
        The hash method must be implemented for actions to be inserted into sets 
        and dictionaries.
        @return: The hash value of the action.
        '''
        return hash(self.name)
    
    def __str__(self):
        '''
        @return: The string representation of this object when *str* is called.
        '''
        return str(self.name)
    
    def __repr__(self):
        return self.__str__()
    
#Global Directions
RIGHT = Direction("right", 0, 1)
LEFT = Direction("left", 0, -1)
UP = Direction("up", -1, 0)
DOWN = Direction("down", 1, 0)
