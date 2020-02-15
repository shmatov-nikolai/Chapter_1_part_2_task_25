'''
Напишите функцию которая находит самою длинную слово в строке.
'''

def leght_string_word(string):
    string = string.split(' ')
    index = 0
    for i in range(0,len(string)):
        if len(string[index]) < len(string[i]):
            index = i
    print(f"в данной строке, самое длинное слово это: '{string[index]}'")



string = "Напишите функцию которая находит самою длинную слово в строке."
leght_string_word(string)
