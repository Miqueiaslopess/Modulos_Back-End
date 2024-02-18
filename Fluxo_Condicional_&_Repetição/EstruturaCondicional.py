
"""falso = False
verdadeiro = True

if verdadeiro == True:
    print("Verdadeiro")
else:
    print("Falso")"""

# ----------------Cadastro------------------#

# -----------------Dados do Cartão------------------#
numero_cartao = 5502099566751016
senha = 1412
codigo_de_seguranca = 567

# -----------------Tela do Usuario------------------#
numero_cartao_digitado = int(input("Digite Numero do seu cartão: "))
senha_digitada = int(input("Digite a senha do seu cartão: "))
codigo_de_seguranca_digitado = int(input("Digite o código de segurança do seu cartão: "))

# -----------------Verificação de Dados------------------#

# pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_digitado
# print(pode_efetuar_pagamento)
if (codigo_de_seguranca == codigo_de_seguranca_digitado) & (senha == senha_digitada) & (numero_cartao == numero_cartao_digitado):
    print("Pagamento efetuado com Sucesso!")
else:
    print("Pagamento Negado!, Verifique os dados digitados e tente novamente.")
