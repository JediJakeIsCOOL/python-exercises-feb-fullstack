#1

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        self.greeting_count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        print("greeting count",self.greeting_count)

    def print_contact_info(self):
        print(self.name+ "'s email: "+ self.email+ ", "+ self.name + "'s phone number: "+ self.phone)
    def add_friend(self,addedfriend):
        self.friends.append(addedfriend)
    def num_friends(self):
        return len(self.friends)
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
        
    

#1.1
sonny = Person('Sonny', 'sonny@hotmail.com', '484-485-4948',)        
print(sonny.name, sonny.email)
#1.2
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456',)
#1.3
Person.greet(sonny, jordan)
#1.4
Person.greet(jordan, sonny)
#1.5
print(sonny.email, sonny.phone)
#1.6
print(jordan.email, jordan.phone)

#2.2
sonny.print_contact_info()
jordan.friends.append(sonny)
sonny.friends.append(jordan)
print(jordan.friends[0].name)
print(len(jordan.friends))
lenny = Person('lenny', 'lenny@lenny.com', '845-554-5454')
jordan.add_friend(lenny)
print(jordan.friends[1].name)
print(sonny.friends[0].name)
print(jordan.num_friends())
Person.greet(jordan, sonny)
Person.greet(jordan, sonny)
print(jordan)

'''
#2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
    def print_info(self):
        print(self.make, self.model, self.year)

myCar = Vehicle('Toyota','Camry','2012')
myCar.print_info()
'''