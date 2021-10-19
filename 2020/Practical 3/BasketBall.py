record = []
class Player:
    def __init__(self, name):
        self.__name = name
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name


class BasketballPlayer(Player):
    positions = ['Guard', 'Forward', 'Center']
    def __init__(self, name):
        super().__init__(name)
    def set_position(self, position):
        self.__position = position
    def get_position(self):
        return self.__position
    def __str__(self):
        return f"{Player.get_name(self)} playing as a {self.__position}"
team_name = input("Enter the basket ball team name: ")
for x in range(5):
    p = BasketballPlayer(input("Enter player name: "))
    while 1:
        check = input("What position is he/she playing?").lower().capitalize()
        if check in BasketballPlayer.positions:
            p.set_position(check.lower().title())
            break
        print("Select a proper position!")
    record.append(p)
print(f"Team {team_name} consists of the following players:")
for x in record:
    print(x)

