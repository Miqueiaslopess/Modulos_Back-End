print("--------------- randon -----------------")

# Importando o módulo random
import random
# Escolhendo um número aleatório dentro de uma Lista
escolha = random.choice([1, 2, 3])
print(escolha)

# Gerando numero aleatório entre 0 e 1
# Multiplicando por 100 para gerar um número entre 0 e 100
numero_aleatorio = random.random() * 100
print(int(numero_aleatorio))  # Convertendo para inteiro

print("--------------- math -----------------")

# Importando o módulo math
import math
# Potência
potencia = math.pow(10, 3)  # 10 elevado a 3
print(potencia)

# Arredondamento
num = math.ceil(10.1)  # Arredondando para cima
print(num)

# Raiz quadrada
raiz = math.sqrt(100)  # Raiz quadrada de 100
print(raiz)

print("--------------- time -----------------")

# Importando o módulo time
from time import time

# Tempo atual em milissegundos
print(time())

#sleep
from time import time, sleep # Importando a função sleep do módulo time

sleep(1)  # Dormindo por 2 segundos

print("--------------- Apelidos -----------------")

# Importando o modulo datetime com um apelido
from datetime import datetime as dt

print(dt.now())  # Data e hora atual

print(dt.now().day)  # Dia atual

print(dt.now().year)  # Ano atual

print(dt.now().month)  # Mês atual

print(dt.now().hour)  # Hora atual

print(dt.now().minute)  # Minuto atual

print(dt.now().second)  # Segundo atual

print(dt.now().microsecond)  # Microsegundo atual


