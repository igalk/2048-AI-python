from problem_agent import ProblemAgent, NO_LIMIT
from search.best_first import BestFirstGraphSearch


class BasicAgent(ProblemAgent):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, problem_state, time_limit=NO_LIMIT):
        return BestFirstGraphSearch(time_limit).find(problem_state, self.heuristic)
