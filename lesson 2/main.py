import math
import matplotlib.pyplot as matplotlib


def task1(n, m):
    inner_i_sum_first = 0
    for i in range(1, n + 1):
        inner_j_sum_first = 0
        for j in range(1, m + 1):
            inner_j_sum_first += math.ceil(i) - 76 * j
        inner_i_sum_first += inner_j_sum_first

    inner_i_sum_second = 0
    for i in range(1, n + 1):
        inner_j_sum_second = 0
        for j in range(1, m + 1):
            inner_j_sum_second += 42 * j + 90 * j ** 4 - 8
        inner_i_sum_second += inner_j_sum_second

    return 22 * inner_i_sum_first - inner_i_sum_second / 31


def task2(n):
    if n == 0:
        return 6
    elif n == 1:
        return 4
    else:
        return 1 / 45 * task2(n - 2) ** 3 + math.cos(task2(n - 1))


def task3(y: list, z: list):
    result = 0
    for i in range(0, len(y)):
        result += (y[i] - z[i]) ** 2
    return math.sqrt(result)


def task4(y: list, z: list):
    result = 0
    for i in range(0, len(y)):
        result += math.fabs(y[i] - z[i])
    return result


def task5(y: list, z: list):
    a = []
    for i in range(3):
        a.append(abs(y[i] - z[i]))
    return max(a)


def task6(y: list, z: list):
    result = 0
    for i in range(0, len(y)):
        result += (y[i] - z[i]) ** 2
    return result


def task7(y: list, z: list):
    h = 5
    result = 0
    for i in range(0, len(y)):
        result += math.fabs(y[i] - z[i]) ** h
    return result ** (1 / h)


def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = matplotlib.subplots()
    # построение гистограммы с подписями
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])


def task8():
    y = [1, 0.5, 1]
    z = [0.5, 2, 1]
    functions = [task3, task4, task5, task6, task7]
    visualize(functions, y, z, move=1)
    matplotlib.show()
    visualize(functions, y, z, move=0.01)
    matplotlib.show()
    visualize(functions, y, z, move=1.5)
    matplotlib.show()


def task9(words: list):
    for i in range(len(words) - 1, 0 - 1, -1):
        if i != 0:
            print(words[i], end=" ")
        else:
            print(words[i])


def count_character(line: str, char):
    return line.count(char.lower()) + line.count(char.upper())


def task10(words: list):
    dictionary = {}
    line = " ".join(words)
    for word in line:
        for char in range(0, len(word)):
            if not dictionary.__contains__(word[char].upper()) and not dictionary.__contains__(word[char].lower()):
                if word[char] != " ":
                    dictionary[word[char].lower()] = count_character(line, word[char])
                else:
                    dictionary[word[char].lower()] = (int)(count_character(line, word[char]) / 2)
    return dictionary


def main():
    print("Task1: ")
    print("f(88,80) = " + '{:.2e}'.format(task1(88, 80)))
    print("f(21,83) = " + '{:.2e}'.format(task1(21, 83)))
    print()

    print("Task2: ")
    print("f(12) = " + '{:.2e}'.format(task2(12)))
    print("f(2) = " + '{:.2e}'.format(task2(2)))
    print()

    y = [1, 0.5, 1]
    z = [0.5, 2, 1]
    print("y: " + str(y))
    print("z: " + str(z))
    print()

    print("Task3: ")
    print("f(y,z) = " + '{:.2e}'.format(task3(y, z)))
    print()

    print("Task4: ")
    print("f(y,z) = " + format(task4(y, z)))
    print()

    print("Task5: ")
    print("f(y,z) = " + format(task5(y, z)))
    print()

    print("Task6: ")
    print("f(y,z) = " + format(task6(y, z)))
    print()

    print("Task7: ")
    print("f(y,z) = " + '{:.3e}'.format(task7(y, z)))
    print()

    task8()

    words = ["language!", "programming", "Python", "the", "love", "I"]
    print("words: " + str(words))
    print()

    print("Task9: ")
    task9(words)
    print()

    print("Task10: ")
    temp = task10(words)
    print(task10(words[::-1]))
    print()


if __name__ == '__main__':
    main()
