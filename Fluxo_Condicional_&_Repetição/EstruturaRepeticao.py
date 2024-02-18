# --------------- Estrutura de Repetição for/in --------------- #

# for <variável> in <sequência>:
c = ['A', 'B', 'C']

for char in c:
    print(char)
# --------------- for/in/range --------------- #
# for <variável> in range(<início>, <fim>, <passo>):+
soma = 0
for valor in range(1, 10):
    soma += valor
    print(soma)

# --------------- EX 02 --------------- #
for multiplo_dois in range(2, 1, 2):
    print(multiplo_dois)

# --------------- EX 03 --------------- #
frutas = ['banana', 'maçã', 'uva', 'pera', 'laranja']

for fruta in frutas:
    print(fruta)

# --------------- EX 04 --------------- #
frase = 'Fala pessoal, meu nome é Andre Perez'

for caracter in frase:
    if (caracter == 'A') | (caracter == 'z'):
        print(f'A letra "{caracter}" está na frase.')
