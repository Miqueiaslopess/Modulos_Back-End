# Uso do Braek e Continue
for i in range(0, 10*10*10):
    print(i)
    if i == 5:
        break

# --------------- EX 02 --------------- #
numero = 10

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')

# --------------- EX 03 --------------- #
# Achando o primeiro número par de uma lista
numeros = [361, 553, 194, 13, 510, 33, 135]

for numero in numeros:
    if numero % 2 == 0:
        print(f'O número {numero} é par')
        break
    else:
        continue
        print(f'O número {numero} é impar')
# sempre que o continue é executado, o código volta para o início do loop, sem executar o código abaixo dele
# sempre que o break é executado, o código sai do loop
# o continue não é muito utilizado, pois é mais fácil colocar o código que se quer executar no else
