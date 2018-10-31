#!/usr/bin/python3

"""
leitura de notas
> 7 aprovado
> 3  <  7 recuperação
caso contrario reprovado
"""
# para resolver um problema pensar em 3 partes entrada, execução e saida

# entrada
qtdNotas = int(input("Digite a quantidade de notas: "))

soma = 0
for x in range(qtdNotas):
    nota = float(input("Digite a nota{}: ".format(x+1)))
    soma += nota

# execução
media = soma / qtdNotas

if int(media) >= 7:
    resultado = "aprovado"
elif int(media) > 3 and int(media) < 7:
    resultado = "recuperacao"
else:
    resultado = "reprovado"

# saida
print("Resultado: {} com media final {}".format(resultado, media))