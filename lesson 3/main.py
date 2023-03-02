import sys
import random

#TODO 6.2; 7.1

text_generator_table = [["Коллеги", "В то же время", "Однако", "Тем не менее", "Следовательно", "Соответственно", "Вместе с тем", "С другой стороны"],
                        ["парадигма цифровой экономики", "контекст цифровой трансформации","диджитализация бизнес-процессов","прагматичный подход к цифровым платформам",
                         "совокупность сквозных технологий", "программа прорывных исследований", "ускорение блокчейн-транзакций", "экспоненциальный рост Big Data"],
                        ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски", "расширяет горизонты", "заставляет искать варианты", "не оставляет шанса для", "повышает вероятность", "обостряет проблему",],
                        ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта", "компрометации конфиденциальных", "универсальной коммодитизации", "несанкционированной кастомизации", "нормативного регулирования", " практического применения"],
                        ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.", "сударственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
                        ]


def generate_groups(groups: list):
    all_type_of_groups = dict()
    for group in groups:
        all_type_of_groups[group[:4]] = []
    for group in groups:
        all_type_of_groups[group[:4]].append(group)

    for key in all_type_of_groups.keys():
        print(key)
        count = 1
        for value in all_type_of_groups[key]:
            if count % 10 == 0:
                print(value)
            else:
                print(value, end=" ")
            count += 1
        print('\n')


def my_print(*values, end='\n', sep=" "):
    sys.stdout.write(sep.join(map(str, values)) + end)


def generate_text():
    length = random.randint(1, 8)
    msg = ""
    for sentence in range(length):
        for part in range(5):
            text = ""
            while text in msg and text == "":
                text = text_generator_table[part][random.randint(0, 7)]
            msg += text + " "
    return msg


print(generate_text())
