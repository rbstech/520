#!/usr/bin/python3

quadrados = []

for x in range(1,11):
        quadrados.append((lambda y: y **2)(x))

print(quadrados)

#list compression melhor performace
quadrados2 = [x ** 2 for x in range(1,11)]

quadrados3 = list(map(lambda x: x ** 2, range(1,11)))
map()

#corrigir grafias 
# pesquisar sobre programacao funcional, geralmente mais utilizada em inteligencia artificial

