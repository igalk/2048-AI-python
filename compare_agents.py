import random
import time
from numbers_problem import NumbersState
from numbers_problem2 import NumbersState2

problem1 = NumbersState.random_start()
problem2 = NumbersState2.random_start()

t1 = 0
t2 = 0

for i in xrange(10000):
    start = time.time()
    s1 = problem1.get_successors()
    t1 += time.time() - start
    if s1:
        problem1 = random.choice(s1.values()).mutate()
    else:
        problem1 = NumbersState.random_start()

    start = time.time()
    s2 = problem2.get_successors()
    t2 += time.time() - start
    if s2:
        problem2 = random.choice(s2.values()).mutate()
    else:
        problem2 = NumbersState2.random_start()

print t1
print t2
