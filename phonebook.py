
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth':'484-585-2923'
}
import pickle

while True:
    print("Electronic Phone Book")
    print("=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")
    print("6. Save all entries")
    print("7. Load saved entries")
    userinp = int(input("What would you like to do?"))


    if userinp == 1:
        inputname = input("Who's number do you want to look up? ")
        for key, value in phonebook_dict.items():
            if inputname == key:
                print(value)
    if userinp ==5:
            break
    if userinp == 2:
        nameentry = input("What is the name you want to enter?")
        phoneint = input("What is there number?")
        phonebook_dict[nameentry] = phoneint
    if userinp == 3:
        delentry = input("Whos name do you want to delete?")
        del phonebook_dict[delentry]
    if userinp == 4:
        print(phonebook_dict)
    if userinp == 6:
        myfile = open('phonebook.pickle', 'wb')
        pickle.dump(phonebook_dict, myfile)
        myfile.close
    if userinp == 7:
        myfile = open('phonebook.pickle', 'rb')
        phonebook_dict = pickle.load(myfile)
    # save the pickle