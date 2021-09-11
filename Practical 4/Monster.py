import random

def display_info(object):
    try:
        object.get_name()
        return object
    except AttributeError:
        return "Invalid monster type"

class Monster:
    def __init__(self, name, health, attack, defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__attack
    def get_defence(self):
        return self.__defence
    def set_name(self, name):
        self.__name = name
    def set_health(self, health):
        self.__health = health
    def set_attack(self, attack):
        self.__attack = attack
    def set_defence(self, defence):
        self.__defence = defence
    def __str__(self):
       return f"{Monster.get_name(self)} is a monster"

class FireMonster(Monster):
    def __init__(self):
        super().__init__("firebug", 10, 9, 4)
    def __str__(self):
        return f"{FireMonster.get_name(self)} is a Fire Type monster"
class WaterMonster(Monster):
    def __init__(self):
        super().__init__("waterbird", 15, 6, 3)
    def __str__(self):
        return f"{WaterMonster.get_name(self)} is a Water Type monster"

class GrassMonster(Monster):
    def __init__(self):
        super().__init__("grasshopper", 20, 5, 3)
    def __str__(self):
        return f"{GrassMonster.get_name(self)} is a Grass Type monster"

class MonsterGame:
    def __init__(self):
        self.choose_monster('None')
        self.generate_monster()
        self.play()
    def choose_monster(self, player_monster):
        self.__player_monster = player_monster
        while 1:
            try:
                self.__player_monster = [FireMonster(), WaterMonster(), GrassMonster()][["F", "W", "G"].index(player_monster)]
                break
            except ValueError:
                player_monster = input("Choose your monster (F, W or G): ").upper().strip()

    def generate_monster(self, computer_monster = [FireMonster(), GrassMonster(), WaterMonster()][random.randint(0,2)]):
        self.__computer_monster = computer_monster
    def play(self):

        while 1:
            self.__computer_monster.set_health(max(self.__computer_monster.get_health() - (self.__player_monster.get_attack() - self.__computer_monster.get_defence()), 0))
            print(f"{self.__computer_monster.get_name()} suffers {self.__player_monster.get_attack() - self.__computer_monster.get_defence()}, the health is {self.__computer_monster.get_health()}")
            if self.__computer_monster.get_health() <= 0:
                print("You Win!")
                break
            self.__player_monster.set_health(max(self.__player_monster.get_health() - (self.__computer_monster.get_attack() - self.__player_monster.get_defence()), 0))
            print(f"{self.__player_monster.get_name()} suffers {self.__computer_monster.get_attack() - self.__player_monster.get_defence()}, the health is {self.__player_monster.get_health()}")
            if self.__player_monster.get_health() <= 0:
                print("You Lost!")
                break
MonsterGame()