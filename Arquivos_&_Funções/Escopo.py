# Escopo da função

def soma_lista(numeros: list) -> int:
    s = 0  # Variável local
    for numero in numeros:
        s += numero
    return s

soma = soma_lista(numeros=[1] * 20)
print(f'Soma: {soma}')

#print(f'Variável s: {s}')  # NameError: name 's' is not defined

# Estrutura de repetição/ Condicinal
if True: #
    x = 100
else:
    w = 50 

print(f'Variável x: {x}') # Se a condição for verdadeira, a variável x será criada
#print(f'Variável w: {w}') # Se a condição for falsa, a variável W não será criada
