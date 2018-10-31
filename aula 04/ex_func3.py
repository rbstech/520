#!/usr/bin/python3

def ler_arquivo(nArquivo):
    ''' Funcao para ler arquivo 
    -> str nome do arquivo
    return -> list conteudo do arquivo
    '''
    with open(nArquivo,'r') as arq:
        return arq.readlines()

def escrever_arquivo(nArquivo, conteudo):
    
    with open(nArquivo,'a') as arq:
        arq.write(conteudo + "\n")


if __name__ == '__main__'
    print('hello')
