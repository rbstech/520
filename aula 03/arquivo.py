#!/usr/bin/python3

# utilize with para garantir que o arquivo foi aberto
#with open('teste.txt','r') as arq:
#    print(arq.read())
#    print(arq.readline())
#    print(arq.readline())
#    print(arq.tell()) ## cursor em bytes 
    ## seek() função para posicinar o cursor que recebe o parametro em bytes
#    print(arq.readline())

lista = ['a\n', 'b\n', 'c\n']
with open('teste.txt','a') as arq:
    arq.write('estou escrevendo lero no arquivo \n')
    #arq.writelines(lista)
    for x in lista:
        arq.write('{}\n'.format(x))
        
# arq = open('teste.txt','r')
# print(arq.read())
# arq.close()
