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

