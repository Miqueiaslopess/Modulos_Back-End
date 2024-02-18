# Progamação Funcional - lambda
# variavel = lambda paramtros: expressao
# --------------- EXEMPLO 1 ---------------- #
print('--------------- EXEMPLO 1 ----------------')
extrair_provedor_email = lambda email: email.split('@')[-1]

email = 'miqueiaslopes@gmail.com'
print(email)

provedor_email = extrair_provedor_email(email)
print(provedor_email)

# --------------- EXEMPLO 2 ---------------- # 
print('--------------- EXEMPLO 2 ----------------')
numero_e_par = lambda numero: True if numero % 2 == 0 else False

numeros = range(0,10)

for numero in numeros:
    if numero_e_par(numero):
        print(f'{numero} é par')

# --------------- EXEMPLO 3 ---------------- #
print('--------------- EXEMPLO 3 ----------------')
#definicao de funcao
def retorno (juros: float):
    return lambda investimento: investimento * (1 + juros)

#isntanciaçao de funcao
retorno_5_porcento = retorno(0.05)
retorno_10_porcento = retorno(0.10)

valor_final = retorno_5_porcento(investimento = 1000)
print(valor_final)

valor_final = retorno_10_porcento(investimento = 1000)
print(valor_final)

ano = 10 
valor_inicial = 1000
valor_final = valor_inicial

for ano in range(1, ano + 1):
    valor_final = retorno_5_porcento(investimento = valor_final)

valor_inicial = round(valor_final, 2)
print(valor_final)

ano = 10 
valor_inicial = 1000
valor_final = valor_inicial

for ano in range(1, ano + 1):
    valor_final = retorno_10_porcento(investimento = valor_final)

valor_inicial = round(valor_final, 2)
print(valor_final)

