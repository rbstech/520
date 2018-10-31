#!/usr/bin/python3

fruta = ["Laranja", "Melancia", "Uva"]

letras = ["a","b","c"]

# For com a var "X" incrementada automaticamente
# Opcional ao for existe o list comprehensions (maior performace para trabalhar com grande volume de dados)
for x in letras[::-1]:
    print(x)

for f in fruta:
    print(f)

# passo
numeros = list(range(60,100,2))
print(numeros)

# passo negativo
numeros = list(range(100,60,-1))
print(numeros)

# sempre que precisar appendar conteudo em uma lista é necessário cria-la primeiro
letras = []

# for de 97 ate 97+26 (97,98,99...) e append (guardando) o valor da tabela ANSI
for x in range(97,97+26):
    letras.append(chr(x))

print(letras)

# exemplo list Comprehensions
# letras = 

# echo \#\!$(which python3) - maneira de automatizar a criação da XB..

