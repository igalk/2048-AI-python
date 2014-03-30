class ProblemState:
    def get_successors(self):
        """
        Generates all the actions that can be performed from this state, and
        the States those actions will create.

        @return: A dictionary containing each action as a key, and its state.
        """
        raise NotImplementedError()

    def get_mutations(self):
        """
        All automated changes to the state happening between moves.
        """
        raise NotImplementedError()

    def mutate(self):
        """
        Perform a single mutation and return the new state.
        """
        raise NotImplementedError()

    def is_goal(self):
        """
        @return: Whether this Problem state is the searched goal or not.
        """
        raise NotImplementedError()

    def __cmp__(self, other):
        """
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly
        positive if self > other.
        """
        raise NotImplementedError()

    def __hash__(self):
        """
        The hash method must be implemented for states to be inserted into sets
        and dictionaries.
        @return: The hash value of the state.
        """
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        return self.__str__()
