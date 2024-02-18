juros = [0.05, 0.07, 0.02, 0.08]
print(juros)

# Inserir um Elemento Sem Substituir: list.insert(index, val)
juros.insert(0, 0.10)
print(juros)

# Inserir um Elemento no Fim da  Lista: list.append(val)
juros.append(0.25)
print(juros)

# Remover um Elemento Pelo Valor: list.remove(val)
juros.remove(0.07)
print(juros)

# Remover um Elemento Pelo Índice: list.pop(val)
terceiro_juros = juros.pop(2)
print(terceiro_juros)

#Conversão
email = 'miqueiaslopes@gmail.com'
caracteres_email = list(email)
print(caracteres_email)

# Trasacoes com append
dia_11_saldo_inicial = 1000

dia_11_trasacoes = []

dia_11_trasacoes.append(243)
dia_11_trasacoes.append(-798.58)
dia_11_trasacoes.append(427.12)
dia_11_trasacoes.append(-10.91)
print(dia_11_trasacoes)

dia_11_saldo_final = dia_11_saldo_inicial + dia_11_trasacoes[0] + dia_11_trasacoes[1] + dia_11_trasacoes[2] + dia_11_trasacoes[3]
print(dia_11_saldo_final)


