
nome = input('digite o nome do arquivo: ')
shebang = '#!/usr/bin/python3 \n'

try:
    # abre arquivo com x, se não existir cria o arquivo
    with open(nome+".py",'x') as arq:
        arq.write(shebang)
except FileExistsError:
    with open(nome+".py",'r') as arq:
        conteudo = arq.readlines()

    if conteudo: # para o python se a lista for vazio é nulo
        if conteudo[0] != shebang:
            conteudo.insert(0, shebang)

        with open(nome+".py", 'w') as arq:
            arq.writelines(conteudo)
    else:
        with open(nome+".py", 'a') as arq:
            arq.write(shebang)
            
        