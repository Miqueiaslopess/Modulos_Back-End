# --------------- EXEMPLO 1 ---------------- #
print('--------------- EXEMPLO 1 ----------------')
numeros = [1, 2, 3]

num_ao_cubo = map(lambda numero: numero ** 3, numeros)
print(list(num_ao_cubo))

# --------------- EXEMPLO 2 ---------------- #
print('--------------- EXEMPLO 2 ----------------')
emails = ['miqueiaslopes@gmail.com', 'miqueiaslopes@live.com', 'mqiueiaslopes@yahoo.com']
# ---------- Dando Nome a Funcao ---------- #
extrair_provedor_email = lambda email: email.split('@')[-1]
# ---------- Codigo mais Imperativo ---------- #
provedores = []
for email in emails:
    provedor = extrair_provedor_email(email)
    provedores.append(provedor)
print(provedores)
# ---------- Codigo Funcional ---------- #
provedores = list(map(extrair_provedor_email, emails))
print(provedores)
# Funcao sem nome
# ---------- Funcao Sem Nome ---------- #
provedores = list(map(lambda email: email.split('@')[-1], emails))
print(provedores)

# --------------- EXEMPLO 3 ---------------- #
print('--------------- EXEMPLO 3 ----------------')
anos = [10, 10, 10]
taxas_juros = [0.05, 0.10, 0.15]
valores_iniciais = [1000, 1000, 1000]

def retorno (valor_inicial: float, taxa_juros: float, ano: int):
    valor_final = valor_inicial
    for ano in range(1, ano + 1):
        valor_final = valor_final * (1 + taxa_juros)
    return round(valor_final, 2)

cenarios = list(map(retorno, valores_iniciais, taxas_juros, anos))
print(cenarios)