import random
import time
from heuristic.basic import BasicHeuristic
from heuristic.basic2 import BasicHeuristic2
from numbers_problem import NumbersState
from numbers_problem2 import NumbersState2

problem1 = NumbersState.random_start()
h1 = BasicHeuristic()
problem2 = NumbersState2.random_start()
h2 = BasicHeuristic2()

t1 = 0
t2 = 0

for i in xrange(10000):
    start = time.time()
    s1 = problem1.get_successors()
    t1 += time.time() - start
    if s1:
        start = time.time()
        mutations = random.choice(s1.values()).get_mutations()
        [h1.evaluate(m[0]) for m in mutations]
        t1 += time.time() - start
        problem1 = random.choice(mutations)[0]
    else:
        problem1 = NumbersState.random_start()

    start = time.time()
    s2 = problem2.get_successors()
    t2 += time.time() - start
    if s2:
        start = time.time()
        mutations = random.choice(s2.values()).get_mutations()
        [h2.evaluate(m[0]) for m in mutations]
        problem2 = random.choice(mutations)[0]
        t2 += time.time() - start
    else:
        problem2 = NumbersState2.random_start()

print t1
print t2
