# Aplica uma funcao a todos os elementos de uma colecao, dois a dois, e retorna apenas um elemento
# variavel = reduce(funcao, colecao)

# --------------- EXEMPLO 1 ---------------- #
print('--------------- EXEMPLO 1 ----------------')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce

soma = reduce(lambda x, y: x + y, numeros)
print(soma)

# --------------- EXEMPLO 2 ---------------- #
print('--------------- EXEMPLO 2 ----------------')
investimentos_clientes_2020 = [1000, 2000, 3000, 4000, 5000]
investimentos_clientes_2021 = [1000, 2000, 3000, 4000, 6000]

# from functools import reduce

total_investido_clientes_2020 = reduce(lambda x, y: x + y, investimentos_clientes_2020)
print(total_investido_clientes_2020)

total_investido_clientes_2021 = reduce(lambda x, y: x + y, investimentos_clientes_2021)
print(total_investido_clientes_2021)

# --------------- EXEMPLO 3 ---------------- #
print('--------------- EXEMPLO 3 ----------------')
# Encontrar o maior numero entre
primeiro = 10
segundo = 11

def maior_entre(primeiro: int, segundo: int) -> int:
    return primeiro if primeiro >= segundo else segundo

print(maior_entre(primeiro=primeiro, segundo=segundo))

# --------------- EXEMPLO 4 ---------------- #
print('--------------- EXEMPLO 4 ----------------')
# Usando Random para gerar uma lista de numeros aleatorios

from random import random #importa a funcao random
print(random())

numeros = [round (100 * random()) for _ in range(0, 100)] 
print(numeros)

maior_numero = reduce(maior_entre, numeros)
print(maior_numero)

