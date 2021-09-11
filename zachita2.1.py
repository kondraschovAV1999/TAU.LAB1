import math  # импортируем необходимые библиотеки
import operator
import random


def roll_dice(dice_type=6):  # Функция, отвечающая за случайный урон персонажами, а также за случайную инициативу.
    return random.randint(1, dice_type)


def sumHealth(unitList):
    # Функция необходимая для подсчета здоровья всех персонажей в фракции для подведения итогов боя,
    # если прошли все 30 раундов
    sumHealth = 0
    for unit in unitList:
        sumHealth += unit.current_HP
    return sumHealth


def remove_defeated(creature_list):  # Функция удаляющая умерших персонажей
    result_list = list(filter(lambda unit: not unit.is_defeat, creature_list))
    defeated_list = list(filter(lambda unit: unit.is_defeat, creature_list))
    if defeated_list:
        print(','.join('%s' % unit.get_name() for unit in defeated_list) + ' defeated')
    return result_list


def check_battle_results(creature_list):  # Проверка результатов боя
    if not creature_list:
        return True
    first_fraction = creature_list[0].fraction
    for unit in creature_list:
        if first_fraction != unit.fraction:
            return False
    return True


class Creature:  # Создаем исходный класс
    def __init__(self, name, fraction, maxHP, power):  # с помощью конструктора создаем класс
        self.name = name  # атрибут, отвечающий за имя существа
        self.fraction = fraction  # атрибут, отвечающий за фракцию существа
        self.maxHP = maxHP
        self.power = power
        self.current_HP = self.maxHP
        self.initiative = 0
        self.is_defeat = False
        self.godShield = False

    def do_action(self, unitList):  # метод класса, отвечающий за дейсвтия персонажа
        enemy = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                enemy.append(unit)
        if not enemy:
            print("Нет врагов")
        else:
            self.attack(unitList, target=enemy[0])

    def attack(self, unitList, target):  # метод для атаки персонажем
        if not target.godShield:
            damage = roll_dice(self.power)
            print(f'{self.get_name()} deal {damage} damage to {target.get_name()}')
            target.get_damage(damage, unitList)
        else:
            damage = 0
            print(f'{target.get_name()} block damage to {self.get_name()} ')
            target.get_damage(damage, unitList)
            target.godShield = False

    def get_damage(self, count, unit_list):  # метод отвечающий за получение урона, и смерть персонажа
        self.current_HP = self.current_HP - count
        if self.current_HP <= 0:
            self.current_HP = 0
            self.is_defeat = True
            self.god_shield(unit_list)

    def get_name(self):  # метод для получения имени персонажа
        return self.name

    def god_shield(self, unitList):
        for unit in unitList:
            if unit.fraction == self.fraction and not unit.is_defeat:
                unit.godShield = True
                break

# unit_list = []
# vasya = Creature('Vasya', 'Human', 10, 3)
# kolya = Creature('Kolya', 'Human', 8, 2)
# peter = Creature('Peter', 'Goblin', 6, 1)
# unit_list.append(vasya)
# unit_list.append(kolya)
# peter.do_action(unit_list)


class Human(Creature):  # Создаем класс людей, наследников класса существа
    def __init__(self, name, creature_fraction):  # вызаваем конструктор класса для создания класса
        base_human_power = 10
        base_human_max_hp = 20
        Creature.__init__(self, name, creature_fraction, base_human_max_hp, base_human_power)

    def get_name(self):
        return "Human " + self.name


class Goblin(Creature):
    def __init__(self, name, creature_fraction):
        base_goblin_power = 4
        base_goblin_max_hp = 10
        Creature.__init__(self, name, creature_fraction, base_goblin_max_hp, base_goblin_power)

    def get_name(self):
        return "Goblin " + self.name


class Dwarf(Creature):
    def __init__(self, name, creature_fraction):
        base_dwarf_power = 4
        base_dwarf_max_hp = 35
        Creature.__init__(self, name, creature_fraction, base_dwarf_max_hp, base_dwarf_power)
        self.damage = roll_dice(self.power)  # Собственный урон каждого отдельного дворфа в первый ход

    def get_name(self):
        return "Dwarf " + self.name

    def attack(self, unitList, target):  # Переопределяем родительский метод
        if not target.godShield:
            damage = roll_dice(self.power)
            print(f'{self.get_name()} deal {damage} damage to {target.get_name()}')
            target.get_damage(damage, unitList)
            self.damage = math.ceil(1.5 * self.damage)  # Собственный урон объекта
        else:
            damage = 0
            print(f'{target.get_name()} block damage to {self.get_name()} ')
            target.get_damage(damage, unitList)
            target.godShield = False


statIn = open('stat.txt')  # открываем файл, созданный для чтения результатов прошлых матчей
lastMathStat = statIn.readline().split()
dictWins = {'Heroes': int(lastMathStat[0]), 'Evils': int(lastMathStat[1]), 'Ничьих': int(lastMathStat[2])}
# Заполняем словарь прошлыми итогами матчей
# Далее создаем персонажей
unit_list = []
goblinList = [Goblin('Klo-Klo', 'evil'), Goblin('Klak-Klak', 'evil'), Goblin('Bax-Bax', 'evil'),
              Goblin('Bax-Bax', 'evil'), Dwarf('Tulin', 'evil')]
humanList = [Human('Boris', 'Hero'), Human('Vitya', 'Hero')]
dwarfList = [Dwarf('Durin', 'Hero')]
unit_list.extend(goblinList)
unit_list.extend(humanList)
unit_list.extend(dwarfList)
for unit in unit_list:
    unit.initiative = roll_dice()
unit_list.sort(key=operator.attrgetter('initiative'), reverse=True)  # Определяем очередность ходов персонажей
is_battle_over = False
round_number = 1
max_round = 30
while not is_battle_over and round_number <= max_round:  # Непосредственно битва
    unit = unit_list.pop(0)  # Достаем первого персонажа из списка персонажей (удалая его при этом)
    unit.do_action(unit_list)  # Персонаж делает свой ход
    unit_list.append(unit)  # Затем после его хода добавляем его в конце списка
    unit_list = remove_defeated(unit_list)  # Удаляем из списка
    is_battle_over = check_battle_results(unit_list)  # проверяем кончился ли бой
    print('round', round_number)
    round_number += 1
if is_battle_over:  # Если бой закончился, то выводим тех персонажей, которые победили
    print(', '.join('%s' % unit.get_name() for unit in unit_list) + ' win ')
    if unit_list[0].fraction == 'Hero':  # Определяем фракцию победивших персонажей и заносим победу в статистику
        dictWins['Heroes'] += 1
    else:
        dictWins['Evils'] += 1
else:  # Если прошли все 30 раундов, то проверяем по здоровью ту сторону, которая выиграла
    healthHeroes = sumHealth(list(filter(lambda unit: unit.fraction == 'Hero', unit_list)))
    healthEvils = sumHealth(list(filter(lambda unit: unit.fraction == 'evil', unit_list)))
    if healthHeroes > healthEvils:
        print('won Heroes')
        dictWins['Heroes'] += 1
    elif healthHeroes < healthEvils:
        print('won Evils')
        dictWins['Evils'] += 1
    else:
        print('Ничья')
print('Статистика боев:')
print('Heroes wins =', dictWins['Heroes'])
print('Evils wins =', dictWins['Evils'])
print('Ничьих =',  dictWins['Ничьих'])
statOut = open('stat.txt', 'w')  # в этом режиме из файла удаляется вся информация и заносится новая
for elem in dictWins.values():  # Заносим статистику текущего боя в файл
    print(elem, file=statOut, end=' ')
statIn.close()
# Защита Вар 1:
# Божественный щит
# Следующий союзник из вашей фракции получает неуязвимость на один удар
# божественный щит дается при смерти
