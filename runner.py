from heuristic.basic import BasicHeuristic
from numbers_problem import *
from problem_agent import ProblemAgent, NO_LIMIT
from search.best_first import BestFirstGraphSearch
import profile

class TestAgent(ProblemAgent):
    def solve(self, problem_state, time_limit=NO_LIMIT):
        return BestFirstGraphSearch(5).find(problem_state, BasicHeuristic())


def print_solution(problem, solution):
    print problem
    current = problem
    for action in solution:
        current = current.get_successors()[action]
        print current
    print 'Solution:', solution
    print 'Solution length:', len(solution)


def main():
    # problem = NumbersState.random_start()
    problem = NumbersState.from_table(
            [[2, 4, 8, 16],
             [2, 32, 2, 32],
             [8, 16, 4, 64],
             [16, 2, 128, 4]])
    print problem

    agent = TestAgent()

    # number_of_moves = 5
    while not problem.is_goal() and problem.get_successors():
        solution = agent.solve(problem, 0)
        print solution
        problem = problem.get_successors()[solution]
        print problem
        if not problem.is_goal():
            problem = problem.mutate()
            print problem
        # number_of_moves -= 1
        # if number_of_moves == 0:
        #     break

# profile.run("main()")
main()