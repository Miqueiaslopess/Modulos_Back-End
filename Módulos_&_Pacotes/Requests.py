import requests as req # Importa a biblioteca requests
import json  # Importa a biblioteca json

# Faz a requisição para a URL
r = req.get('www.python.org.br/')

# Imprime o status da requisição
print(r.status_code)
print(r.text)

# Converte o texto da requisição para um dicionário
data = json.loads(r.text)
print(data)

# Itera sobre o dicionário para encontrar a taxa CDI
cdi = None

# Itera sobre o dicionário para encontrar a taxa CDI
for key, value in data.items():
    if key == 'taxa':
        cdi = value.replace(',', '.')
        cdi = float(cdi)

print(cdi)
