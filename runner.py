from numbers_problem import *
from problem_agent import ProblemAgent, NO_LIMIT
from search.algorithm import Heuristic
from search.best_first import BestFirstGraphSearch


class TestAgent(ProblemAgent):
    def solve(self, problem_state, time_limit=NO_LIMIT):
        return BestFirstGraphSearch(1).find(problem_state, TestHeuristic())


class TestHeuristic(Heuristic):
    def evaluate(self, state):
        score = 0
        b = state.board
        while b > 0:
            curr = b & ALL_ONES
            if curr > 0:
                score += (curr / 2 - 1)
            else:
                score += 32
            b = (b >> CELL_SIZE)
        # TODO give score for adjacent empty cells
        return score


def print_solution(problem, solution):
    print problem
    current = problem
    for action in solution:
        current = current.get_successors()[action]
        print current
    print 'Solution:', solution
    print 'Solution length:', len(solution)


problem = NumbersState.random_start()
print problem

agent = TestAgent()

while not problem.is_goal():
    solution = agent.solve(problem, 0)
    print solution
    problem = problem.get_successors()[solution]
    print problem
    if not problem.is_goal():
        problem = problem.mutate()
        print problem
