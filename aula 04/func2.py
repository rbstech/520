#!/usr/bin/python3


# Args e kwargs

# ao passar multiplos parametros a funcao transforma em uma tupla
def parametros(*args):
    print(args)

parametros('Robson','nome',5,[],{})