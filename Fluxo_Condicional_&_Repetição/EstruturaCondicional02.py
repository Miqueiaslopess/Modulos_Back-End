# --------------- Tratamento de Erro try/except ----------------#
# O tratamento de erro é uma forma de evitar que o programa pare de funcionar caso o usuário digite um valor inválido.
preco = float(input("Digite o valor total da conta: "))
pessoas = 0

try:
    pessoas = int(input("Digite o numero de pessoas: "))
    valor_por_pessoa = preco/pessoas
    print("O valor por pessoa é de: R$", valor_por_pessoa)
except ZeroDivisionError:
    print("Valor inválido, digite um numero inteiro maior que 0.")

# Outro exemplo de tratamento de erro:
anos = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
try:
    ano_atual = int(input("Digite o ano atual: "))
    print("O ano atual é: ", anos[ano_atual])
except IndexError:
    print("Valor inválido, digite um numero inteiro entre 0 e 7.")
