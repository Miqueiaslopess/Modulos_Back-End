print('---------------- WRITE ----------------')
from Leitura import idades # Importando a lista de idades

# Escrevendo a lista de idades em um arquivo
print('---------- Modo (w)write ----------')
with open(file='idades.csv', mode='w', encoding='utf8') as fp:
    linha = 'Idade' + '\n'
    fp.write(linha)
    for idade in idades:
        linha = str(idade) + '\n'
        fp.write(linha)


print('---------- Modo (a)append ----------')
# Adicionando a lista de idades em um arquivo
with open(file='idades.csv', mode='a', encoding='utf8') as fp:
    for idade in idades:
        linha = str(idade + 100) + '\n'
        fp.write(linha)


