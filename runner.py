from numbers_problem import *
from problem_agent import ProblemAgent
from search.algorithm import Heuristic
from search.best_first import BestFirstGraphSearch
import time

class TestAgent(ProblemAgent):
    def solve(self, problem_state, time_limit):
        return BestFirstGraphSearch().find(problem_state, TestHeuristic())

class TestHeuristic(Heuristic):
    def evaluate(self, state):
        score = 0
        b = state.board
        while b > 0:
            curr = b&ALL_ONES
            if curr > 0:
                score += (curr/2-1)
            b = (b>>CELL_SIZE)
        return score

def printSolution(problem, solution):
    print problem
    current = problem
    for action in solution:
        current = current.getSuccessors()[action]
        print current
    print 'Solution:', solution
    print 'Solution length:', len(solution)


problem = NumbersState.randomStart()
print problem

agent = TestAgent()

start = time.clock()
solution = agent.solve(problem, 0)
run_time = time.clock() - start

printSolution(problem, solution)
print 'Running time:', run_time
