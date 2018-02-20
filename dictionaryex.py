'''
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth':'484-585-2923'
}
print(phonebook_dict['Elizabeth'])

phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)

del phonebook_dict['Alice']
print(phonebook_dict)

phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

for value in phonebook_dict.values():
    print(value)

#2
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])

#3
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

#4
def letters(paragraph):
    diction = {}
    for chars in paragraph:
        if chars not in diction:

def wordnum(sentence):
    word_list = sentence.split()
    word_lib = {}
    for x in word_list:
        if x not in word_lib:
            word_lib[x] = 1
        else:
            word_lib[x] += 1
    print(word_lib)

wordnum('this is this is this is cool')
'''
words= 'this is this is this is cool'.split()
print(words)
