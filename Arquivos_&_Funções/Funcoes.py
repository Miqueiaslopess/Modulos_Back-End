# Voce trabalha na bolsa de valores e precisa simular o retorno de um investimento para diversos cenaarios
print('------------------ EXEMPLO 01 ------------------')
# Codigo Mais Imperativo
valor_inicial, taxa_juros_anual, anos = 1000, 0.05, 10

valor_final = valor_inicial 
for ano in range(1, anos + 1):
    valor_final = valor_final * (1 + taxa_juros_anual)
valor_final = round(valor_final, 2)
print(f'Para um investimento inicial de R$ {valor_inicial} com uma taxa de juros anual de {taxa_juros_anual * 100}% durante {anos} anos, o valor final será de R$ {valor_final}')


valor_inicial, taxa_juros_anual, anos = 1020, 0.03, 10

valor_final = valor_inicial
for ano in range(1, anos + 1):
    valor_final = valor_final * (1 + taxa_juros_anual)
valor_final = round(valor_final, 2)
print(f'Para um investimento inicial de R$ {valor_inicial} com uma taxa de juros anual de {taxa_juros_anual * 100}% durante {anos} anos, o valor final será de R$ {valor_final}')


print('------------------ EXEMPLO 02 ------------------')
#------------------ Funções ------------------
def imprime(mensagem: str):
    print(mensagem)

texto = 'Olá mundo' 

imprime(texto)

print('------------------ EXEMPLO 03 ------------------')

def maiusculo(texto: str)-> str:
    text_maiusculo = texto.upper()
    return text_maiusculo

nome = 'Miqueias'
print(nome)

nome_maisculo = maiusculo(texto=nome)
print(nome_maisculo)

print('------------------ EXEMPLO 04 ------------------')

# Dedinindo uma funcao que recebe um texto e retorna o texto em maiusculo
def extrair_usuario_email_provedor(email: str) -> (str, str):
    email_separado = email.split(sep='@')
    usuario = email_separado[0]
    provedor = email_separado[1]
    return usuario, provedor

#Declaração de variaveis
email = 'miqueias@gmail.com'

#Chamada da função
usuario , provedor = extrair_usuario_email_provedor(email=email)

#Impressão dos resultados
print(f'Usuario: {usuario}')
print(f'Provedor: {provedor}')

#------------------ PARAMETROS ------------------

print('------------------ EXEMPLO 05 ------------------')
# Funcao sem Parametros

def pi( )-> float:
    return 3.14159265359
pi= pi()
print(pi)

print('------------------ EXEMPLO 06 ------------------')

def imprime_pi( ) -> None:
    print(3.14159265359)
    return None
imprime_pi()
