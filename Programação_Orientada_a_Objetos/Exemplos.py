# Tudo no python é um objeto

# Exemplo 1
tipos = [type(10), type(10.0), type('Ebac'), type([1, 2, 3]), type({1, 2, 3}), type({'janeiro': 1}), type((1, 2, 3)), type(True)], type(None), type(lambda x: x)

for tipo in tipos:
    print(tipo) 