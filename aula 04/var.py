#!/usr/bin/python3

# variavel global - definida pela indentacao
var = 10

def escopo():
    global var
    var = 5
    print(var)

escopo()
print(var)

