try:
    letras = ['a','b']

    print(letras[2])

except IndexError as e:
    print('a lista contem apenas {} elementos'.format(
        len(letras)
        # Em python sempre que existir parenteses podemos quebrar linha
    ))
    print(e)

letras = ['a','b']
ling = {'Robson': 'Python'}
print(ling.get('Robson'))