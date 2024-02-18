endereco = 'Avenida Paulista, 1811, São Paulo, São Paulo, Brasil.'

# Maiusculo: string.upper()
print(endereco.upper())


# Posição: string.find(substring)
posicao = endereco.find('Brasil')
print(posicao)


# Substituição: string.replace(antigo, novo)
print(endereco.replace('Avenida', 'Av'))

# ---------- Convesões de String em Inteiro ---------------
idade = 20
print(type(idade)) 

#idade virou Sting
idade = str(idade)
print(type(idade))

# ---------- Convesões de String em Inteiro ---------------
faturamento = 'R$35 mi'
print(type(faturamento))

faturamento = int(faturamento[2:5])
print(faturamento)
print(type(faturamento))


#----------------Problema------------------#

# Sua Emepresa
lat = '-22.005320'
lon ='-47.891040'

# Startup Adquirida
latlon = '-22.005320; -47.891040'

# Encontrando a posicao do caracter 
posicao_char_divisao = (latlon.find(';'))
#print(posicao_char_divisao)

# Extraindo a latitude
lat_startup = (latlon[0:posicao_char_divisao])
#print(lat_startup)

# Extraido a Longitude
lon_startup = latlon [posicao_char_divisao+1:len(latlon)]

#----------Interação Interface----------#
print (f"A Longitude é:{lon_startup}" )
print (f"A Latitude é: {lat_startup}" )



