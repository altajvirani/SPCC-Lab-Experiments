from string import ascii_letters

Keywords = ['void', 'int', 'float', 'double', 'char', 'short', 'long', 'return',
            'typeof', 'sizeof', 'if', 'else', 'do', 'while', 'break', 'continue', 'for']
Operators = {
    'Arithemetic': ['+', '-', '*', '/', '%'],
    'Assignement': ['=', '+=', '-=', '*=', '/=', '%='],
    'Comparision': ['==', '!=', '<=', '>=', '<', '>'],
    'Logical': ['&&', '||']
}
Punctuation = [',', ';', ':', '?']
HeaderFile = ['<stdio.h>', '<conio.h>']
SpecialSymbol = '( ) { } ! & $ # @'
BuiltInFun = ['printf', 'scanf', 'main']
PreProcessor = ['#include', '#define']
SetData = set()
FileData = open(r"LEX\\ccode.c", "r")
Tokens = FileData.read().split()

print("{:<15} {:15}" .format("Lexemes", "Tokens"))
print('-'*50)
for i in Tokens:
    if i in Keywords:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, "Keyword"))
    elif i in Operators['Arithemetic']:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Arithemetic Operator'))
    elif i in Operators['Assignement']:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Assignment Operator'))
    elif i in Operators['Comparision']:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Comparision Operator'))
    elif i in Operators['Logical']:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Logical Operator'))
    elif i in Punctuation:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Punctuation'))
    elif i in HeaderFile:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'HeaderFile'))
    elif i in SpecialSymbol:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'SpecialSymbol'))
    elif i in PreProcessor:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'PreProcessor'))
    elif i in BuiltInFun:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'BuiltInFun'))
    elif i in ascii_letters:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Identifiers'))
    else:
        if i not in SetData:
            SetData.add(i)
            print("{:<15}{:<15}".format(i, 'Constant'))
