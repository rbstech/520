
try:
    n = input('Digite um numero: ')
    n = int(n)
    if n % 2 == 0:
        print('par')
    else:
        print('impar')

except ValueError:

    #comentada a list compression e feito com for + append
    res = [ord[x] for x in n]
    #for x in n:
    #    res.append(n)
    
    res = sum(res)
    if res % 2 == 0:
        print('par {}'.format(res))
    else:
        print('impar {}'.format(res))

except Exception:
    print('Tratamento generico')

print('não parei a execução')