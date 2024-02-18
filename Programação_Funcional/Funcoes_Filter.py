# Aplica uma funcao logica ( que retorna True ou False) a cada elemento de uma colecao(list,dict,etc.)
# E Retorna uma colecao apenas com aqueles que resultam verdadeiro(true)
# variavel = filter(funcao_logica, colecao)                                                               

# --------------- EXEMPLO 1 ---------------- #
print('--------------- EXEMPLO 1 ----------------')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_par = filter(lambda num: num % 2 == 0, numeros)
numeros_impar = filter(lambda num: num % 2 != 0, numeros)

print(list(numeros_par))
print(list(numeros_impar))

# --------------- EXEMPLO 2 ---------------- #
print('--------------- EXEMPLO 2 ----------------')
emails = ['miqueiaslopes@gmail.com', 'miqueiaslopes@live.com', 'mqiueiaslopes@yahoo.com']
provedor_da_google = lambda email:'gmail' in email

# ---------- Codigo mais Imperativo ---------- #
emails_google = []
for email in emails:
    if provedor_da_google(email):
        emails_google.append(email)

print(emails_google)
# ---------- Codigo Funcional ---------- #
emails_google = filter(provedor_da_google, emails)
print(list(emails_google))