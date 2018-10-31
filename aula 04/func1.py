#!/usr/bin/python3

# duplo underscore __ usando "dund" para chamar funcoes magicas*

#def somente define a funcao que somente sera executada ao ser chamada
def funcao():
    return "hello world"

a = funcao()
print(a)
print(funcao().title())

# parametros quando eu defino a funcao
# diferenca entre parametros e argumentos / somente conceito, mas usualmente chamada apenas de parametros ou argumentos
def somar(x,y):
    return x + y

# argumentos quando eu chamo a funcao
print(somar(somar(3,5),somar(2,2)))

# parametros nomeados
somar(y=2,x=6)

# funcao com parametro default
somar2(x,y=5)

# o sistema considera o y default e soma 3 passado na fun
print(somar2(3))

# utilizado em funcao para pular a execução pass
# muito comum quando vc inicia a criação de uma função, mas não termina

