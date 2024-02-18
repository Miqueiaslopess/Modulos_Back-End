# --------------------- METODOS --------------------- #

artigo = dict(
    titulo = 'Modulo 02 | Aula 03 - Dicionarios',
    corpo = 'Topicos, Aulas, Listas, Conjuntos, Dicionarios...',
    total_caracteres = 1530
)
print(artigo)
print(type(artigo))

#Adicionar/Atualizar um elemento pela chave-valor: dict.update(dict) #
print('Atualiando um elemento pela chave-valor')
print(artigo)
artigo.update({'total_caracteres': 7850})
print(artigo)

#Remover um elemento pela chave: dict.pop(chave) #
print('Removendo um elemento pela chave')
artigo.pop('total_caracteres')
print(artigo)