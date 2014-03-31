from basic_agent import BasicAgent
from numbers_problem import *


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

    agent = BasicAgent()

    # number_of_moves = 5
    while not problem.is_goal() and problem.get_successors():
        solution = agent.solve(problem, 5)
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