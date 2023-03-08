import math
import sys
import random
import time
from graphviz import Digraph


# 5.1
groups = ['ИВБО-01-21', 'ИВБО-02-21', 'ИВБО-03-21', 'ИВБО-04-21', 'ИВБО-05-21', 'ИВБО-06-21', 'ИВБО-07-21',
          'ИВБО-08-21',
          'ИКБО-01-21', 'ИКБО-02-21', 'ИКБО-03-21', 'ИКБО-03-21', 'ИКБО-04-21', 'ИКБО-05-21', 'ИКБО-06-21',
          'ИКБО-07-21', 'ИКБО-08-21',
          'ИКБО-09-21', 'ИКБО-10-21', 'ИКБО-11-21', 'ИКБО-12-21', 'ИКБО-13-21', 'ИКБО-14-21', 'ИКБО-15-21',
          'ИКБО-16-21', 'ИКБО-17-21',
          'ИКБО-18-21', 'ИКБО-19-21', 'ИКБО-20-21', 'ИКБО-21-21', 'ИКБО-22-21', 'ИКБО-23-21', 'ИКБО-24-21',
          'ИКБО-25-21', 'ИКБО-26-21',
          'ИКБО-27-21', 'ИКБО-28-21', 'ИКБО-29-21', 'ИКБО-30-21', 'ИКБО-31-21', 'ИКБО-32-21', 'ИКБО-33-21',
          'ИМБО-01-21', 'ИМБО-02-21',
          'ИНБО-01-21', 'ИНБО-02-21', 'ИНБО-03-21', 'ИНБО-03-21', 'ИНБО-04-21', 'ИНБО-05-21', 'ИНБО-06-21',
          'ИНБО-07-21', 'ИНБО-08-21',
          'ИНБО-09-21', 'ИНБО-10-21', 'ИНБО-11-21', 'ИНБО-12-21', 'ИНБО-13-21']


def generate_groups():
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


# 5.2
def my_print(*values, end='\n', sep=" "):
    sys.stdout.write(sep.join(map(str, values)) + end)


# 6.1
text_generator_table = [
    ["Коллеги", "В то же время", "Однако", "Тем не менее", "Следовательно", "Соответственно", "Вместе с тем",
     "С другой стороны"],
    ["парадигма цифровой экономики", "контекст цифровой трансформации", "диджитализация бизнес-процессов",
     "прагматичный подход к цифровым платформам",
     "совокупность сквозных технологий", "программа прорывных исследований", "ускорение блокчейн-транзакций",
     "экспоненциальный рост Big Data"],
    ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски", "расширяет горизонты",
     "заставляет искать варианты", "не оставляет шанса для", "повышает вероятность", "обостряет проблему", ],
    ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
     "компрометации конфиденциальных", "универсальной коммодитизации", "несанкционированной кастомизации",
     "нормативного регулирования", " практического применения"],
    ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.",
     "сударственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.",
     "внезапных открытий."]
]


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


# 6.2
fnames = ['Александр', 'Артём', 'Михаил', 'Максим', 'Иван', 'Даниил', 'Дмитрий', 'Матвей', 'Кирилл', 'Андрей']
tnames = ['Александрович', 'Артёмович', 'Михайлович', 'Максимович', 'Иваныч', 'Данилович', 'Дмитриевич', 'Матвеевич',
          'Кириллович', 'Андреевич']
snames = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Фёдоров']


def generate_names():
    for i in range(10):
        fname_index = int(time.time() * 13 + math.sin(time.time()) + 34734) % 10
        tname_inex = int(time.time() * math.cos(time.time() % 100)) % 10
        sname_index = int(time.time()) % 10
        time.sleep(1)
        print(fnames[fname_index], " ", tnames[tname_inex], " ", snames[sname_index])


dict_exit = {'room': 'Выход'}
dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7, dict_8, dict_9, dict_10, dict_11, dict_12, dict_13, dict_14, dict_15, dict_16 = dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict()
dict_1['Вверх'], dict_1['Влево'], dict_1['info'], dict_1[
    'room'] = dict_exit, dict_2, 'Вы находитесь в комнате', 'Комната №1'
dict_2['Вправо'], dict_2['Влево'], dict_2['info'], dict_2[
    'room'] = dict_1, dict_3, 'Вы находитесь в комнате', 'Комната №2'
dict_3['Вправо'], dict_3['Влево'], dict_3['info'], dict_3[
    'room'] = dict_2, dict_4, 'Вы находитесь в комнате', 'Комната №3'
dict_4['Вправо'], dict_4['Влево'], dict_4['Вверх'], dict_4['info'], dict_4[
    'room'] = dict_3, dict_5, dict_7, 'Вы находитесь в комнате', 'Комната №4'
dict_5['Вправо'], dict_5['Влево'], dict_5['info'], dict_5[
    'room'] = dict_4, dict_6, 'Вы находитесь в комнате', 'Комната №5'
dict_6['Вправо'], dict_6['Вверх'], dict_6['info'], dict_6[
    'room'] = dict_5, dict_7, 'Вы находитесь в комнате', 'Комната №6'
dict_7['Вниз'], dict_7['Вверх'], dict_7['info'], dict_7[
    'room'] = dict_6, dict_8, 'Вы находитесь в комнате', 'Комната №7'
dict_8['Вниз'], dict_8['Вверх'], dict_8['Вправо'], dict_8['info'], dict_8[
    'room'] = dict_7, dict_9, dict_16, 'Вы находитесь в комнате', 'Комната №8'
dict_9['Вниз'], dict_9['Вверх'], dict_9['info'], dict_9[
    'room'] = dict_8, dict_10, 'Вы находитесь в комнате', 'Комната №9'
dict_10['Вниз'], dict_10['Вправо'], dict_10['info'], dict_10[
    'room'] = dict_9, dict_11, 'Вы находитесь в комнате', 'Комната №10'
dict_11['Вправо'], dict_11['Влево'], dict_11['info'], dict_11[
    'room'] = dict_10, dict_12, 'Вы находитесь в комнате', 'Комната №11'
dict_12['Влево'], dict_12['Вниз'], dict_12['info'], dict_12[
    'room'] = dict_11, dict_13, 'Вы находитесь в комнате', 'Комната №12'
dict_13['Вверх'], dict_13['Вниз'], dict_13['info'], dict_13[
    'room'] = dict_12, dict_14, 'Вы находитесь в комнате', 'Комната №13'
dict_14['Вверх'], dict_14['Вниз'], dict_14['Влево'], dict_14['info'], dict_14[
    'room'] = dict_13, dict_15, dict_16, 'Вы находитесь в комнате', 'Комната №14'
dict_15['Вверх'], dict_15['Вниз'], dict_15['info'], dict_15[
    'room'] = dict_14, dict_4, 'Вы находитесь в комнате', 'Комната №15'
dict_16['Влево'], dict_16['Вправо'], dict_16['info'], dict_16[
    'room'] = dict_8, dict_14, 'Вы находитесь в комнате', 'Комната №16'


# 7.1
def game(spawn: dict):
    currentRoom = spawn
    while currentRoom['room'] != 'Выход':
        print(currentRoom['room'], '\n', currentRoom['info'])
        for key in currentRoom.keys():
            if key != 'info' and key != 'room':
                print('> ', key)
        choice = ''
        while choice not in currentRoom.keys():
            choice = input('>>> ')
        currentRoom = currentRoom[choice]
    print("Вы вышли из лабиринта!")


# 7.2
dot = Digraph('graph', strict=True)
dot.node(dict_14['room'], dict_14['room'])
rooms = set()


def createDot(point: dict):
    for room in point.keys():
        if room != 'info' and room != 'room':
            if not rooms.__contains__(point[room]['room']):
                dot.node(point[room]['room'], point[room]['room'])
                rooms.add(point[room]['room'])
                createDot(point[room])
            dot.edge(point['room'], point[room]['room'])
            if point[room]['room'] != 'Выход':
                dot.edge(point[room]['room'], point['room'])
        else:
            return


createDot(dict_14)
dot.render('graph.gv')
