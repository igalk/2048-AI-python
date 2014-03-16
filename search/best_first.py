#####################################
##                                 ##
##   Best-First Search Algorithm   ##
##                                 ##
#####################################

# This is an implementation of the SearchAlgorithm interface for the following
# search algorithms:
# - BestFirstGraphSearch

import time
from algorithm import SearchAlgorithm

infinity = 1.0e400


class State:
    def __init__(self, state, score, orig_direction, chance):
        self.state = state
        self.score = score
        self.orig_direction = orig_direction
        self.chance = chance

    def search(self, heuristic):
        mutations = self.state.get_mutations()
        states = []
        for mutation, chance in mutations.iteritems():
            best = {'score': -1, 'successor': None, 'chance': 0}
            successors = mutation.get_successors()
            for successor in successors.itervalues():
                score = heuristic.evaluate(successor)
                if score > best['score']:
                    best['score'] = score
                    best['successor'] = successor
                    best['chance'] = chance
            if best['successor']:
                states.append(State(best['successor'], best['score'], self.orig_direction, self.chance * best['chance']))

        return states


class BestFirstGraphSearch(SearchAlgorithm):
    """
    Implementation of a best-first search algorithm for the Problem.
    This is inherently a greedy algorithm, as it takes the best possible action
    at each junction with no regard to the path so far.
    It may also take a maximum depth at which to stop, if needed.
    """

    def __init__(self, time_limit=infinity, max_depth=infinity):
        """
        Constructs the best-first graph search.
        Optionally, a maximum depth may be provided at which to stop looking for
        the goal state.
        """
        self.time_limit = time_limit
        self.max_depth = max_depth

    def find(self, problem_state, heuristic):
        """
        Search the nodes with the lowest heuristic evaluated scores first.
        You specify the heuristic that you want to minimize.
        For example, if the heuristic is an estimate to the goal, then we have
        greedy best first search.
        If the heuristic is the depth of the node, then we have DFS.
        Optionally a limit may be supplied to limit the depth of the seach.

        @param problem_state: The initial state to start the search from.
        @param heuristic: A heuristic function that scores the Problem states.
        """
        start = time.time()

        scores = {}
        states = []
        successors = problem_state.get_successors()
        for direction, new_state in successors.iteritems():
            score = heuristic.evaluate(new_state)
            scores[direction] = score
            states.append(State(new_state, score, direction, 1.0))

        best_move = {'score': -1, 'direction': -1}
        moves = 0
        while (time.time() - start) < self.time_limit:
            # Find the current best state
            best_index, best_state = max(enumerate(states), key=lambda state: state[1]  .score)

            # Replace the best state with all its children
            states.pop(best_index)
            children = best_state.search(heuristic)
            score = scores[best_state.orig_direction]
            score -= (best_state.score * best_state.chance)
            for child in children:
                score += (child.score * child.chance)
                states.append(child)

            scores[best_state.orig_direction] = score
            if score > best_move['score']:
                best_move['score'] = score
                best_move['direction'] = best_state.orig_direction

            moves += 1
        print moves
        return best_move['direction']
