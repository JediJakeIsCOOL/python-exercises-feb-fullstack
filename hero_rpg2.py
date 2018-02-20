import random



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
    def __init__(self, herohealth, heropower):
       super().__init__(herohealth, heropower)
    def attack(self, goblin):
        if random.random() < .2:
            print("Critical hit!")
            goblin.health -= self.power * 2
            print("You do"+ self.power *2 +"damage to the enemy")
        else:
            goblin.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    #def __init__(self, goblinhealth, goblinpower):
       #super().__init__(goblinhealth, goblinpower)
    def attack(self, hero):

        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))    
class Medic(Character):
    def print_status(self):
        print("The medic {} health and {} power.".format(self.health, self.power))
    




    
medic1 = Medic(8, 2)
hero1 = Hero(10, 5)
goblin1 = Goblin(6, 2)
    

def main(h, e):
    
    medic1 = Medic(8, 2)
    hero1 = Hero(10, 5)
    goblin1 = Goblin(6, 2)
    while e.alive() and h.alive():
        h.print_status()
        e.print_status()
        
        print()
        print("What do you want to do?")
        print("1. fight ", e)
        print("2. do nothing")
        print("3. flee")
        print("> ",end=' ' )
        userinp = input()
         
        if userinp == "1":
            h.attack(e)
        elif userinp == "2":
            pass
        elif userinp == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(userinp))

        if e.health > 0:
            e.attack(h)
main(hero1, goblin1)
whatpath = input()
print("You come to a path that has multiple options on which to travel..")
print("Which option do you want to go down?")
print("1. The dark winding alley ")
print("2. Towards a glowing light in the distance")
print("3. Into the cemetary")
main()
