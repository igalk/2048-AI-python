from basic_agent import BasicAgent
from heuristic.basic2 import BasicHeuristic2
from numbers_problem2 import NumbersState2


def print_solution(problem, solution):
    print problem
    current = problem
    for action in solution:
        current = current.get_successors()[action]
        print current
    print 'Solution:', solution
    print 'Solution length:', len(solution)


def main():
    problem = NumbersState2.random_start()
    print problem

    agent = BasicAgent(BasicHeuristic2())

    # number_of_moves = 5
    while problem.get_successors():
        solution = agent.solve(problem, 5)
        print solution
        problem = problem.get_successors()[solution]
        print problem
        if problem.is_goal():
            print 'WIN!!'
            return
        else:
            problem = problem.mutate()
            print problem
        # number_of_moves -= 1
        # if number_of_moves == 0:
        #     break

# profile.run("main()")
main()