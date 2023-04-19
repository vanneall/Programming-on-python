# Task 3.1
import inspect

import numpy as np
from graphviz import Digraph
import matplotlib.pyplot as plt
import sample


def draw(vertices: list, edged: list, num=""):
    for node in vertices:
        dot.node(str(node[0]), node[1])
    for current_edge in edged:
        dot.edge(str(current_edge[0]), str(current_edge[1]))
    dot.render('graph_v' + str(num) + '.gv')


dot = Digraph('graph')
ls = [(1, 'v1'), (2, 'v2')]
ls2 = [(1, 2), (2, 3), (2, 2)]


# draw(ls, ls2)


# Task 3.2
class Chaos:
    def __init__(self, mu: float, state: float):
        self.mu = mu
        self.state = state
        for i in range(1000):
            self.next()

    def stabilize(self):
        pass

    def next(self):
        pass


class LogisticMap(Chaos):
    def next(self):
        super().next()
        self.state = self.mu * self.state * (1 - self.state)
        return self.state


o = LogisticMap(2, 0.1)
print(o.next(), o.next(), o.next())


# Task 3.3
def visualize(logisticMap, num):
    values = []
    edges = []
    val = logisticMap.next()
    values.append((val, str(val)))
    last = val
    while True:
        val = logisticMap.next()
        if values.__contains__((val, str(val))):
            edges.append((last, values[0][0]))
            break
        else:
            values.append((val, str(val)))
            edges.append((last, val))
            last = val
    draw(values, edges, num)


for mu in [2, 3.2, 3.5, 3.55]:
    pass
    # visualize(LogisticMap(mu, 0.1), mu)


# Task 3.4
# μArray = []
# xArray = []
# for μ in np.linspace(1, 4, 30):
#     o = LogisticMap(μ, 0.1)
#     for i in range(10):
#         μArray.append(μ)
#         xArray.append(o.next())
#
# plt.scatter(μArray, xArray)
# plt.show()

# # Task 3.5
# o = LogisticMap(mu=4.0, state=0.1)
# vals = []
# for i in range(100000):
#     vals.append(o.next())
# plt.hist(vals, rwidth=0.9, bins=30)
# plt.show()


# Task 5.1
def documentation(samplee):
    for name, data in inspect.getmembers(samplee):
        if name.startswith('__'):
            continue

        print(data.__doc__)
        documentation(data)


print(str(inspect.getsource(sample.A.meth1)))
documentation(sample)
