# --------------------- Dicionario --------------------- #

brasil = {'capital': 'Brasília' , 'idioma': 'Português', 'população': 210}

print(brasil)
print(type(brasil))
# --------------------- EX.02 --------------------- #
carro = {
    'marca': 'Volkswagen' ,
    'modelo': 'Polo',
    'ano': 2022
}
print(carro)

# --------------------- Dicionarios Compostos --------------------- #
cadastro = {
    'andre': {
    'nome': 'Andre Perez',
    'ano_nascimento': 1992,
    'pais': {
        'pai': {
            'nome' : '<nome_do_pai> Perez',
            'ano_do_nascimento': 1971
        }, 
        'mae' : {
           'nome': 'nome_da_mae Perez' ,
           'ano_nascimento' : 1973
        },  
     }    
    }
}
# --------------------- ATRIBUINDO --------------------- #
print('ATRIBUINDO')
credito = {'123' : 750, '789' : 980}
score_123 = credito ['123']
score_789 = credito ['789']

print(score_123) 
print(score_789)
# --------------------- Substituindo Valores --------------------- #
print('Substituindo Valores')
credito ['123'] = 435 
print(credito)

# --------------------- Acrescentando Valores --------------------- #
print('Acrescentando Valores')
credito['456'] = 1000
print(credito)
