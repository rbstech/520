#!/usr/bin/python3

idade = input('Digite sua idade')
acomp = input('Acompanhado S/N')

if int(idade) >= 18:
    print('permite entrada')
elif int(idade) < 18 and acomp == 'S':
    print('permite entrada')
else:
    print('entrada proibida')