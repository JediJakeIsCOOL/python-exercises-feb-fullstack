
class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
class Hero(Character):
    #def __init__(self, herohealth, heropower):
      # super().__init__(herohealth, heropower)
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    #def __init__(self, goblinhealth, goblinpower):
      # super().__init__(goblinhealth, goblinpower)
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))    




def main():
   
    hero1 = Hero(10, 5)
    goblin1 = Goblin(6, 2)
    while goblin1.alive() and hero1.alive():
        hero1.print_status()
        goblin1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",end=' ' )
        userinp = input()
         
        if userinp == "1":
            hero1.attack(goblin1)
        elif userinp == "2":
            pass
        elif userinp == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(userinp))

        if goblin1.health > 0:
            goblin1.attack(hero1)
            

main()
