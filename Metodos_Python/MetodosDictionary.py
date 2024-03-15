# Dicionário inicial
meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

# clear(): Remove todos os elementos do dicionário
meu_dicionario.clear()
print("clear: Remove todos os elementos do dicionário. Dicionário atual:", meu_dicionario)

# copy(): Retorna uma cópia do dicionário
copia_dicionario = meu_dicionario.copy()
print("copy: Retorna uma cópia do dicionário. Cópia:", copia_dicionario)

# fromkeys(): Retorna um dicionário com as chaves e valor especificados
novas_chaves = ['x', 'y', 'z']
novo_dicionario = dict.fromkeys(novas_chaves, 0)
print("fromkeys: Retorna um dicionário com as chaves e valor especificados. Novo dicionário:", novo_dicionario)

# get(): Retorna o valor da chave especificada
valor_chave_b = meu_dicionario.get('b')
print("get('b'): Retorna o valor da chave especificada. Valor:", valor_chave_b)

# items(): Retorna uma lista contendo uma tupla para cada par chave-valor
itens_dicionario = meu_dicionario.items()
print("items: Retorna uma lista contendo uma tupla para cada par chave-valor. Itens:", itens_dicionario)

# keys(): Retorna uma lista contendo as chaves do dicionário
chaves_dicionario = meu_dicionario.keys()
print("keys: Retorna uma lista contendo as chaves do dicionário. Chaves:", chaves_dicionario)
# Dicionário inicial
meu_dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Exemplo 1: pop() - Remove o elemento com a chave especificada
chave_removida = 'b'
elemento_removido = meu_dicionario.pop(chave_removida)
print(f"Exemplo 1: pop('{chave_removida}'): Remove o elemento com a chave '{chave_removida}'. Elemento removido:", elemento_removido, "Dicionário atual:", meu_dicionario)

# Exemplo 2: popitem() - Remove o último par chave-valor inserido
ultimo_par = meu_dicionario.popitem()
print(f"Exemplo 2: popitem(): Remove o último par chave-valor inserido. Último par removido: {ultimo_par} Dicionário atual: {meu_dicionario}")

# setdefault(): Retorna o valor da chave especificada e insere a chave com o valor especificado se não existir
valor_chave_c = meu_dicionario.setdefault('c', 0)
print("setdefault('c', 0): Retorna o valor da chave especificada e insere a chave com o valor especificado se não existir. Valor:", valor_chave_c, "Dicionário atual:", meu_dicionario)

# update(): Atualiza o dicionário com os pares chave-valor especificados
meu_dicionario.update({'d': 4, 'e': 5})
print("update: Atualiza o dicionário com os pares chave-valor especificados. Dicionário atual:", meu_dicionario)

# values(): Retorna uma lista de todos os valores no dicionário
valores_dicionario = meu_dicionario.values()
print("values: Retorna uma lista de todos os valores no dicionário. Valores:", valores_dicionario)
