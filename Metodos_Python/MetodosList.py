# Lista inicial
my_list = [1, 2, 3, 4]

# append(): Adiciona um elemento ao final da lista
my_list.append(5)
print(f"Lista após append(5): {my_list}")

# clear(): Remove todos os elementos da lista
my_list.clear()
print(f"Lista após clear(): {my_list}")

# copy(): Retorna uma cópia da lista
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(f"Cópia da lista original: {copied_list}")

# count(): Retorna o número de elementos com o valor especificado
count_twos = original_list.count(2)
print(f"Quantidade de '2' na lista: {count_twos}")

# extend(): Adiciona os elementos de uma lista ao final da lista atual
extended_list = [4, 5, 6]
original_list.extend(extended_list)
print(f"Lista após extend(): {original_list}")

# index(): Retorna o índice do primeiro elemento com o valor especificado
index_of_three = original_list.index(3)
print(f"Índice do primeiro '3': {index_of_three}")

# insert(): Adiciona um elemento na posição especificada
original_list.insert(2, 9)
print(f"Lista após insert(2, 9): {original_list}")

# pop(): Remove o elemento na posição especificada
popped_element = original_list.pop(3)
print(f"Elemento removido com pop(3): {popped_element}, Lista atual: {original_list}")

# remove(): Remove o primeiro item com o valor especificado
original_list.remove(5)
print(f"Lista após remove(5): {original_list}")

# reverse(): Inverte a ordem da lista
original_list.reverse()
print(f"Lista após reverse(): {original_list}")

# sort(): Ordena a lista
original_list.sort()
print(f"Lista após sort(): {original_list}")
