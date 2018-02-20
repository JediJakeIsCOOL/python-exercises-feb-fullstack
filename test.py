'''
list1= [[1, 2], [3,4]]
print(list1[0][1])

userinp = int(input("how big of a square"))
for x in range(0, userinp):

    for y in range(0, userinp):
        print("*",end="")
    print("")

userNum = int(input("What number do you want to know the divisor of?"))

for i in range(1, userNum +1):
    if userNum % i == 0:
        print(i)

lista = [1 , 2 , 3]
print(2 in lista

a = [2, 3 ,4 ,5 ]
b = [2, 3 ,4, 6]
for x in a: 
    if a in b:
        print(x)

userStr = input("Is this word a palindrome?")

if userStr[::-1] == userStr:
    print("This is a palindrome")
else:
    print("Nope")

def Letter(words):
    counts = {}
    for char in words:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    print(counts)

userin = input()

Letter(userin)

counts = {}
counts['a'] = 1
print(counts)

list1 = ["boop", "beep", "bop", "bing"]
for x in list1:
    print(x)

reading = ["boop", "beep", "bop", "bing"]
for x in range(0, len(reading)):
    print(reading[x])

Filename = input("What is the filename? ")
letterHist = {}
wordHist = {}
file_handle = open(Filename, 'r')
reading = file_handle.read()
wordreading = reading.split()
for i in range(0, len(reading)):
    if reading[i] in letterHist:
        letterHist[reading[i]] += 1
    else:
            letterHist[reading[i]] = 1
for i in range(0, len(wordreading)):
    if wordreading[i] in wordHist:
        wordHist[wordreading[i]] += 1
    else:
            wordHist[wordreading[i]] = 1
print(wordHist)
print(letterHist)
'''

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

main()
