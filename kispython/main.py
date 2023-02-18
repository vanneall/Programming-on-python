import math


def task2(y):
    if y < 64:
        return (82 - 16 * y) ** 4 - y ** 3
    elif 64 <= y < 127:
        return 69 * y ** 7
    elif 127 <= y < 207:
        return math.fabs(y) ** 6 - y ** 5
    else:
        return 19 * (1 + y ** 2 + y) + (y ** 3 / 37 + 32 * y) ** 3


def task3(n, b, p):
    resultSum = 0
    for k in range(1, b + 1):
        cSum = 0
        for c in range(1, n + 1):
            cSum += 8 * p ** 7 + 54 * (42 * c ** 3 - 35 * p ** 2) ** 3 + k ** 6
        resultSum += cSum
    return resultSum


def task4(n):
    if n == 0:
        return 0.26
    return (task4(n - 1) ** 2 / 47 - 40 * task4(n - 1)) / 96


def task5(y: list, x: list):
    result = 0
    n = len(y)
    for i in range(1, n + 1):
        y1 = y[n - i] ** 3
        x1 = x[n - math.ceil(i/2)]
        y2 = y[n - i] ** 2
        result += 31 * (y1 + x1 + y2) ** (3/2)
    return 37 * result
