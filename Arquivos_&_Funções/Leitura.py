print('---------------- READ ----------------')
conteudo = None  # Inicializando a variável conteudo

# Abrindo o arquivo em modo de leitura
with open(file='./banco.csv', mode='r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

print(conteudo)

print('---------------- READLINE ----------------')
conteudo = []

with open(file='./banco.csv', mode='r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()  # Lendo a primeira linha
    while linha:
        conteudo.append(linha)
        linha = arquivo.readline()  # Lendo a próxima linha

print(conteudo)

# Imprimindo o conteúdo linha a linha
for linha in conteudo:
    print(linha)

print('---------------- Manipulação De Dados ----------------')

idades = []

with open(file='./banco.csv', mode='r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()  # Lendo o cabeçalho
    linha = arquivo.readline()  # Lendo a primeira linha
    while linha:
        linha_separada = linha.split(',')  # Separando os dados da linha
        idade = linha_separada[0]  # Pegando a idade de cada linha
        idade = int(idade)  # Convertendo a idade para inteiro
        idades.append(idade)  # Adicionando a idade na lista
        linha = arquivo.readline()  # Lendo a próxima linha

print(idades)

# Calculando a média das idades
def media_idades(idades):
    soma = 0
    for idade in idades:
        soma += idade
    return soma / len(idades)


print(f"Media de idade: {media_idades(idades)}")
