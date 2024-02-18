# ---------- TELA USUARIO ----------#
usuario_cadastro = input("Usuario: ")
senha_cadastro = str(input("Senha: "))

# ----------BANCO DE DADOS ----------#
usuario_email = "luciana@gmail.com"
senha = "123456"

# VALIDANDO USUARIO E SENHA
usuario_igual = usuario_cadastro == usuario_email
senha_igual = senha == senha_cadastro

# VALIDANDO ACESSO
conceder_acesso = usuario_igual & senha_igual

if (conceder_acesso):
    print("Login Permitido")

else:
    print("Login Negado")
