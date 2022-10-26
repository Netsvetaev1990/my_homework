class Warrior:
    def __init__(self, name='warrior', health=100, stamina=100):
        self.name = name
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print("--------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Name : {self.name}\n'
              f'Health: {self.health}\n'
              f'Stamina: {self.stamina}')
        print("--------")

    def heals(self, target):
        if self.stamina < 20:
            print("Недостаточный запас сил для лечения травами")
        else:
            print("--------")
            print(f'{self.name} собирает целебные травы и накладывает повязку',
                  f'на {target.name}')
            target.health += 10
            self.stamina -= 20
            print(f'Здоровье у {target.name} повышено до {target.health}\n',
                  f'У {self.name} осталось {self.stamina} единиц сил')
            print("--------")

    def attacks(self, target):
        print("--------")
        print(f'{self.name} наносит урон мечом {target.name}')
        target.health -= 3
        # if target.health <= 0:
        #     print(f'Маг {target.name} убит')
        # else:
        print(f'Здоровье у {target.name} понижено до {target.health}')
        print("--------")

class Mage:
    def __init__(self, name='mage', health=60, mana=100):
        self.name = name
        self.health = health
        self.mana = mana

    def introduces(self):
        print("--------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Name : {self.name}\n'
              f'Health: {self.health}\n'
              f'Mana: {self.mana}')
        print("--------")

    def heals(self, target):
        if self.mana < 20:
            print("Недостаточно маны для заклинания лечения")
        else:
            print("--------")
            print(f'{self.name} применяет заклинание лечения',
                  f'на {target.name}')
            target.health += 10
            self.mana -= 20
            print(f'Здоровье у {target.name} повышено до {target.health}\n',
                  f'У {self.name} осталось {self.mana} единиц маны')
            print("--------")

    def attacks(self, target):
        print("--------")
        print(f'{self.name} наносит урон магией {target.name}')
        target.health -= 3
        # if target.health <= 0:
        #     print(f'Воин {target.name} убит')
        # else:
        print(f'Здоровье у {target.name} понижено до {target.health}')
        print("--------")


unit3 = Mage('Вася')
unit4 = Mage('Женя', health=4, mana=110)

unit1 = Warrior('Денис', stamina=50)
unit2 = Warrior('Никита', 40, 70)

i = 0
while True:
    action = input('Выберите действие: 1 - атака, 2 - лечение: ')
    if action == '1':
        unit_choise = input('Выберите юнита: 1 - Денис, 2 - Никита, 3 - Вася, 4 - Женя: ')
        if unit_choise == '1':
            attack_goal = input('Выберите цель: 2 - Никита, 3 - Вася, 4 - Женя: ')
            if attack_goal == '2':
                unit1.attacks(unit2)
                if unit2.health <= 0:
                    print("Воин Никита убит")
                    break
            elif attack_goal == '3':
                unit1.attacks(unit3)
                if unit3.health <= 0:
                    print("Маг Вася убит")
                    break
            elif attack_goal == '4':
                unit1.attacks(unit4)
                if unit4.health <= 0:
                    print("Маг Женя убит")
                    break
        elif unit_choise == '2':
            attack_goal = input('Выберите цель: 1 - Денис, 3 - Вася, 4 - Женя: ')
            if attack_goal == '1':
                unit2.attacks(unit1)
                if unit1.health <= 0:
                    print("Воин Денис убит")
                    break
            elif attack_goal == '3':
                unit2.attacks(unit3)
                if unit3.health <= 0:
                    print("Маг Вася убит")
                    break
            elif attack_goal == '4':
                unit2.attacks(unit4)
                if unit4.health <= 0:
                    print("Маг Женя убит")
                    break
        elif unit_choise == '3':
            attack_goal = input('Выберите цель: 1 - Денис, 2 - Никита, 4 - Женя: ')
            if attack_goal == '1':
                unit3.attacks(unit1)
                if unit1.health <= 0:
                    print("Воин Денис убит")
                    break
            elif attack_goal == '2':
                unit3.attacks(unit2)
                if unit2.health <= 0:
                    print("Воин Никита убит")
                    break
            elif attack_goal == '4':
                unit3.attacks(unit4)
                if unit4.health <= 0:
                    print("Маг Женя убит")
                    break
    elif action == '2':
        unit_choise = input('Выберите юнита: 1 - Денис, 2 - Никита, 3 - Вася, 4 - Женя: ')
        if unit_choise == '1':
            heals_goal = input('Выберите кого полечим: 2 - Никита, 3 - Вася, 4 - Женя: ')
            if heals_goal == '2':
                unit1.heals(unit2)
            elif heals_goal == '3':
                unit1.heals(unit3)
            elif heals_goal == '4':
                unit1.heals(unit4)
        elif unit_choise == '2':
            heals_goal = input('Выберите кого полечим: 1 - Денис, 3 - Вася, 4 - Женя: ')
            if heals_goal == '1':
                unit2.heals(unit1)
            elif heals_goal == '3':
                unit2.heals(unit3)
            elif heals_goal == '4':
                unit2.heals(unit4)
        elif unit_choise == '3':
            heals_goal = input('Выберите кого полечим: 1 - Денис, 2 - Никита, 4 - Женя: ')
            if heals_goal == '1':
                unit3.heals(unit1)
            elif heals_goal == '2':
                unit3.heals(unit2)
            elif heals_goal == '4':
                unit3.heals(unit4)
i += 1
print("Два на одного. Стоп игра")