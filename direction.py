class Direction():
    """
    A direction of movement.
    """

    def __init__(self, name, dy, dx):
        """
        Creates a new direction.
        @param name: The direction's name.
        """
        self.name = name
        self.dy = dy
        self.dx = dx

    def build_traversals(self):
        x = range(4) if self.dx != 1 else range(3, -1, -1)
        y = range(4) if self.dy != 1 else range(3, -1, -1)
        return {'x': x, 'y': y}

    def __cmp__(self, other):
        """
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly
        positive if self > other.
        """
        return cmp(self.name, other.name)

    def __hash__(self):
        """
        The hash method must be implemented for actions to be inserted into sets
        and dictionaries.
        @return: The hash value of the action.
        """
        return hash(self.name)

    def __str__(self):
        """
        @return: The string representation of this object when *str* is called.
        """
        return str(self.name)

    def __repr__(self):
        return self.__str__()

#Global Directions
RIGHT = Direction("right", 0, 1)
LEFT = Direction("left", 0, -1)
UP = Direction("up", -1, 0)
DOWN = Direction("down", 1, 0)
