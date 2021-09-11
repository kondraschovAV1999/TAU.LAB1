def roll_dice(dice_type=6):
    return random.randint(1, dice_type)

class Creature():
    def __init__(self, name, fraction, maxHP, power):
        self.name = name
        self.fraction = fraction
        self.maxHP = maxHP
        self.power = power
        self.current_HP = self.maxHP
        self.initiative = 0
        self.is_defeat = False


    def do_action(self, unit_list):
        enemy = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                enemy.append(unit)
        if  not enemy:
            print("Нет врагов")
        else:
            self.attack(target = enemy[0])

    def attack(self, target):
        damage = roll_dice(self.power)
        print(f'{self.get_name()} deal {damage} damage to {target.get_name()}')
        target.get_damage(damage)

    def get_damage(self,count):
        self.current_HP = self.current_HP - count
        if self.current_HP <= 0:
            self.is_defeat = True

    def get_name(self):
        return self.name

# unti_list = []
# vasya = Creature('Vasya', 'Human', 10, 3)
# kolya = Creature('Kolya', 'Human', 8, 2)
# peter = Creature('Peter', 'Goblin', 6, 1)
# unti_list.append(vasya)
# unti_list.append(kolya)
# peter.do_action(unti_list)

import random, operator


class Human(Creature):
    def __init__(self, name, creature_fraction):
        base_human_power = 10
        base_human_max_hp = 20
        Creature.__init__(self, name ,creature_fraction ,base_human_max_hp ,base_human_power)
        self.luck = 10


    def get_name(self):
        return "Human " + self.name


class Goblin(Creature):
    def __init__(self,name, creature_fraction):
        base_goblin_power = 4
        base_goblin_max_hp = 10
        Creature.__init__(self, name , creature_fraction, base_goblin_max_hp, base_goblin_power)

    def get_name(self):
        return "Goblin " + self.name


def remove_defeated(creature_list):
    result_list = list(filter(lambda unint: not unit.is_defeat, creature_list ))
    defeated_list = list(filter(lambda unint: unit.is_defeat, creature_list ))
    if defeated_list:
        print(','.join('%s'% unit.get_name() for unit in defeated_list) + ' defeated')
    return result_list


def check_battle_results(creature_list):
    if not creature_list:
        return True
    first_fraction = creature_list[0].fraction
    for unit in creature_list:
        if first_fraction != unit.fraction:
            return False
    return True

unit_list = []
goblin_1 = Goblin('Klo-Klo', 'evil')
goblin_2 = Goblin('Klak-Klak','evil')
human_1 = Human('Boris', 'Hero')
unit_list.append(goblin_1)
unit_list.append(goblin_2)
unit_list.append(human_1)
human_1.do_action(unit_list)
for unit in unit_list:
    unit.initiative = roll_dice()
unit_list.sort(key=operator.attrgetter('initiative'), reverse=True)
is_battle_over = False
round_number = 1
max_round = 30
while not is_battle_over and round_number <= max_round:
    unit = unit_list.pop(0)
    unit.do_action(unit_list)
    unit_list.append(unit)
    unit_list = remove_defeated(unit_list)
    is_battle_over = check_battle_results(unit_list)
    round_number += 1

if  is_battle_over:
    print(', '.join('%s'% unit.get_name() for unit in unit_list) + 'win')
