'''
strNew = "wowza"
print(strNew.upper())

#2
capStr = "woah"
print(capStr.capitalize())

#3
revStr = "bananna"
print(revStr[::-1])

#4
word = input('sweet sentence you want in leetspeak?: ').upper()

word = word.replace('A', '4')
word = word.replace('E', '3')
word = word.replace('G', '6')
word = word.replace('I', '1')
word = word.replace('O', '0')
word = word.replace('S', '5')
word = word.replace('T', '7')

print(word)


#5
extend = input("word with 2 vowels in a row?")
extend = extend.replace("ee", "eeeee")
extend = extend.replace("oo", "ooooo")
print(extend)
'''
#6 
secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
offset = 13
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''

for char in secret:
    ascii_code = ord(char)
    is_uppercase = ascii_code >= 65 and ascii_code <= 90
    char = char.lower()
    if char not in alphabet:
        new_char = char
    else:
        idx = alphabet.find(char)
        new_idx = idx + offset
        if new_idx > 25:
            new_idx = new_idx - 26
        new_char = alphabet[new_idx]
        if is_uppercase:
            new_char = new_char.upper()
    result += new_char

print(result)



