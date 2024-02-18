# --------------------- CONVERSÕES --------------------- #

artigo = dict(
    titulo = 'Modulo 02 | Aula 03 - Dicionarios',
    corpo = 'Topicos, Aulas, Listas, Conjuntos, Dicionarios...',
    total_caracteres = 1530
)
print('Artigo Original ---> ', artigo)
# --------------------- Extraindo Chaves Para Listas --------------------- #
print('----------Extraindo Chaves Para Listas----------')
chaves = list(artigo.keys())
print(chaves)
print(type(chaves))
# --------------------- Extraindo Valores Para Listas --------------------- #
print('----------Extraindo Valores Para Listas----------')
valores = list(artigo.values())
print(valores)
print(type(valores))
# --------------------- Motivação --------------------- # 

wifi_disponiveis = []

rede = {'nome': 'rede1', 'senha:': '123456'}  
wifi_disponiveis.append(rede)

rede = {'nome': 'uai-fi', 'senha:': 'r3d3'}  
wifi_disponiveis.append(rede)

print(wifi_disponiveis)