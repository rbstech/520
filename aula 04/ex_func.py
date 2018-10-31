#!/usr/bin/python3

convidados = []

def adicionar():
    '''funcao para adicionar convidados na lista'''
    global convidados

    qtd = int(input("Digite a quantidade de convidados: "))

    print(qtd)

    for n in range(qtd):
        nome = input('Insira o nome do convidado '+str(n+1)+": ")
        convidados.append(nome)
        
adicionar()

print(convidados)

# professor utilizou while true (while com loop infinito)