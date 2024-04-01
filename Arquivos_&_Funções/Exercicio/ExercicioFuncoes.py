# 1. Funções para arquivo csv
# Complete a função abaixo para extrair uma coluna do arquivo csv em uma lista.
# Os elementos devem ter o tipo de dado correto.
# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
# extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
# use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna = []
    with open(file=nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        linha = arquivo.readline()  # Lendo o cabeçalho
        linha = arquivo.readline()  # Lendo a primeira linha
        while linha:
            linha_separada = linha.split(',')  # Separando os dados da linha
            dado = linha_separada[indice_coluna]  # Pegando o dado da coluna
            if tipo_dado == 'int':
                dado = int(dado)  # Convertendo o dado para inteiro
            elif tipo_dado == 'float':
                dado = float(dado)  # Convertendo o dado para float
            coluna.append(dado)  # Adicionando o dado na lista
            linha = arquivo.readline()  # Lendo a próxima linha
    return coluna

# extrair a coluna valor_venda
valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado='str')
print(valor_venda) # deve retornar ['vhigh', 'med', 'low', ...]

# extrair a coluna pessoas
pessoas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=4, tipo_dado='int')
print(pessoas) # deve retornar [2, 2, 2, ...]

# 2\. Funções para arquivo txt
# Complete a função abaixo para extrair uma as palavras de uma linha do arquivo txt em uma lista.

def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []
    with open(file=nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        for i, linha in enumerate(arquivo):
            if i == numero_linha - 1:
                palavras_linha = linha.split()  # Separando as palavras da linha
                break
    return palavras_linha

# extraindo linha 10
linha10 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=10)
print(linha10) # deve retornar ['Mas', 'eis', 'que', 'chega', 'a', 'roda', 'viva']