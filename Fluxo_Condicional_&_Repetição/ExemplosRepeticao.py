# --------------- EX 01 --------------- #
try:
    frase = 'Fala pessoal, meu nome é Miqueias Lopes'
    letra_de_pesquisa = str(input('Digite uma letra para pesquisar: '))
    letra_de_pesquisa2 = str(input('Digite outra letra para pesquisar: '))

    encontrou_letra1 = False
    encontrou_letra2 = False

    for caracter in frase:
        if caracter == letra_de_pesquisa:
            encontrou_letra1 = True
        elif caracter == letra_de_pesquisa2:
            encontrou_letra2 = True

    if encontrou_letra1 and encontrou_letra2:
        print(f'A letra "{letra_de_pesquisa}" e a letra "{
              letra_de_pesquisa2}" estão na frase.')
    elif encontrou_letra1:
        print(f'A letra "{letra_de_pesquisa}" está na frase, mas a letra "{
              letra_de_pesquisa2}" não está.')
    elif encontrou_letra2:
        print(f'A letra "{letra_de_pesquisa2}" está na frase, mas a letra "{
              letra_de_pesquisa}" não está.')
    else:
        print('Nenhuma das letras está na frase.')

except ValueError:
    print("O valor digitado não é uma letra, tente novamente!")

# --------------- EX 02 --------------- #
credito = {'123': 1000, '456': 2000, '789': 3000}

for chave, valor in credito.items():
    print(f'Para o CPF {chave} o score de crédito é {valor}')
    print('\n')

# --------------- EX 03 --------------- #
credito = {'123': 1000, '456': 2000, '789': 3000}

# Extraindo as chaves e valores do dicionário
for chave, valor in credito.items():
    print(f'Para o CPF {chave} o score de crédito é {valor}')

# Extraindo apenas as chaves do dicionário
for chave in credito.keys():
    print(f'Para o CPF {chave} o score de crédito é {credito[chave]}')

# Extraindo apenas os valores do dicionário
for valor in credito.values():
    print(f'O score de crédito é {valor}, mas não sabemos o CPF.')


