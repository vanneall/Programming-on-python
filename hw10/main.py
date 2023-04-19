# Task 3.1
from graphviz import Digraph


def draw(vertices: list, edged: list):
    for node in vertices:
        dot.node(str(node[0]), node[1])
    for current_edge in edged:
        dot.edge(str(current_edge[0]), str(current_edge[1]))
    dot.render('graph_v.gv')


dot = Digraph('graph')
ls = [(1, 'v1'), (2, 'v2')]
ls2 = [(1, 2), (2, 3), (2, 2)]
#draw(ls, ls2)


# Task 3.2
class Chaos:
    def __init__(self, mu:float, state:float):
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


o = LogisticMap(2, 0.1)
o.next()
print(o.state, end=" ")
o.next()
print(o.state, end=" ")
o.next()
print(o.state, end=" ")
