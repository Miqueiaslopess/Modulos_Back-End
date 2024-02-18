# ---------- Listas ---------- #

fabricantes_mobile_china = ['xiaomi', 'huawei']
fabricantes_mobile_eua = ['apple', 'motorola']
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua

print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile)

print(type(fabricantes_mobile))

# ---------- Descobrir o Posicionamento ----------#
print(f'0: {fabricantes_mobile[0]}')
print(f'-1: {fabricantes_mobile[-1]}')

# ---------- Fatiamento ----------#
fabricantes_mobile_china = fabricantes_mobile[0:2]
fabricantes_mobile_eua = fabricantes_mobile[2:len(fabricantes_mobile)]

print ('CHINA: ' + str(fabricantes_mobile_china))
print ('EUA: ' + str(fabricantes_mobile_eua))

# --------------- Adicionando Elementos na Lista --------------- #
print(fabricantes_mobile)

fabricantes_mobile[2] = 'nokia'
print(fabricantes_mobile)