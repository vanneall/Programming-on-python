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


# o = LogisticMap(2, 0.1)
# print(o.next(), o.next(), o.next())


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
all_fields = set()


def documentation(module, isClass=False, inner_class=None):
    if not all_fields.__contains__(module):
        module = __import__(module)
        print('# Модуль ' + inspect.getmodulename(str(module)[str(module).find('from') + 6:-2]) + '\n')
        print(str(module.__doc__).strip() + '\n')
        all_fields.add(module)
    if isClass:
        for object in inspect.getmembers(inner_class, inspect.isfunction):
            name, value = object
            if not name.startswith('__') and not all_fields.__contains__(value):
                title_func = str(inspect.getsource(value)).split('\n')[0].strip()
                title_func = title_func[title_func.find('def') + 4: -1]
                print('**Метод** \'' + title_func + '\'\n')
                print(str(value.__doc__).strip() + '\n')
                all_fields.add(value)
    for object in inspect.getmembers(module):
        name, value = object
        if inspect.isclass(value) and not all_fields.__contains__(value):
            print('## Класс ' + name + '\n')
            print(str(value.__doc__).strip() + '\n')
            all_fields.add(value)
            documentation(module, isClass=True, inner_class=value)
        if inspect.isfunction(value) and not all_fields.__contains__(value):
            print('## Функция: ' + name + '\n')
            title_func = str(inspect.getsource(value)).split('\n')[0].strip()
            title_func = title_func[title_func.find('def') + 4:-1]
            print('Сигнатура: \'' + title_func + '\'\n')
            print(str(value.__doc__).strip() + '\n')
            all_fields.add(value)


# documentation('sample')


# Task 5.2
from pathlib import Path

all_paths = set()


def draw_ierarchie(path):
    if str(path).endswith('.py') and not all_paths.__contains__(str(path)):
        all_paths.add(str(path))
        return True
    if path.is_dir():
        for x in path.rglob("*"):
            if not str(x).__contains__('venv') and not str(x).__contains__('.git') and not str(x).__contains__(
                    '.idea') and not str(x).endswith('__'):
                if draw_ierarchie(x) == True and not x.is_dir():
                    x = str(x)
                    a = x[:x.rfind('\\')]
                    x = x[a.rfind('\\') + 1:]
                    x = x.replace('\\','/')
                    dot.edge(str(path)[str(path).rfind('\\') + 1:], x)
                elif x.is_dir() and not all_paths.__contains__(str(x)):
                    all_paths.add(str(x))
                    dot.edge(str(path)[str(path).rfind('\\') + 1:], str(x)[str(x).rfind('\\') + 1:])
    return False


#p = Path("D:/Programming/PythonProjects/ProgrammingOnPython")
#draw_ierarchie(p)
#dot.render('graph_draw.gv')

p = Path("C:/")
for x in p.rglob("*"):
    if str(x).__contains__('Visual Paradigm'):
        print(x)
print('КОНЕЦ')
