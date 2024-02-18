try:
    # -----------------Dados do Cartão------------------#
    numero_cartao = 12345
    senha = 1234
    codigo_de_seguranca = 123

    # -----------------Tela do Usuario------------------#
    numero_cartao_digitado = int(input("Digite Numero do seu cartão: "))
    senha_digitada = int(input("Digite a senha do seu cartão: "))
    codigo_de_seguranca_digitado = int(input("Digite o código de segurança do seu cartão: "))

    # -----------------Verificação de Dados------------------#
    if (codigo_de_seguranca == codigo_de_seguranca_digitado) & (senha == senha_digitada) & (numero_cartao == numero_cartao_digitado):
        print("Pagamento efetuado com Sucesso!")
    elif (codigo_de_seguranca != codigo_de_seguranca_digitado) & (senha == senha_digitada) & (numero_cartao == numero_cartao_digitado):
        print("Erro: Codigo de segurança incorreto!")
    elif (codigo_de_seguranca == codigo_de_seguranca_digitado) & (senha != senha_digitada) & (numero_cartao == numero_cartao_digitado):
        print("Erro: Senha incorreta!")
    elif (codigo_de_seguranca == codigo_de_seguranca_digitado) & (senha == senha_digitada) & (numero_cartao != numero_cartao_digitado):
        print("Erro: Numero do cartão incorreto!")
    elif (codigo_de_seguranca != codigo_de_seguranca_digitado) & (senha != senha_digitada) & (numero_cartao == numero_cartao_digitado):
        print("Erro: Codigo de segurança e senha incorretos!")
    elif (codigo_de_seguranca != codigo_de_seguranca_digitado) & (senha == senha_digitada) & (numero_cartao != numero_cartao_digitado):
        print("Erro: Codigo de segurança e numero do cartão incorretos!")
    elif (codigo_de_seguranca == codigo_de_seguranca_digitado) & (senha != senha_digitada) & (numero_cartao != numero_cartao_digitado):
        print("Erro: Senha e numero do cartão incorretos!")
    else:
        print("Pagamento Negado!, Verifique os dados digitados e tente novamente.")
except ValueError:
    print("Erro: Digite apenas numeros!!!.")