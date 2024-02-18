# Carrinho de compras

qtd_itens_carrinho_compra = 0

qtd_itens_carrinho_compra = qtd_itens_carrinho_compra +1
print(qtd_itens_carrinho_compra)

qtd_itens_carrinho_compra = qtd_itens_carrinho_compra -1
print(qtd_itens_carrinho_compra)


# Modo mais simplificado ##
qtd_itens_carrinho_compra = 0

qtd_itens_carrinho_compra += 1
print(qtd_itens_carrinho_compra)

qtd_itens_carrinho_compra += 1
print(qtd_itens_carrinho_compra)


## Conversão de Peso em Preço##

preco_carnePicanha = 100
quantidade_peso = 0.500

total_a_pagar = quantidade_peso * preco_carnePicanha

print(total_a_pagar)

## 19/01 ##
tvv_19_ = 153.98
tqv_19_ = 3

tkt_19_ = (tvv_19_ / tqv_19_)
print ("Media de Ticket do dia 19/01: ", tkt_19_)

##20/01##
tvv_20_ =  337.01
tqv_20_ = 7

tkt_20_ = (tvv_20_ / tqv_20_) 
print ("Media de Ticket do dia 20/01: ", tkt_20_)

# 21/01 #
tvv_21_ = 295.33
tqv_21_ = 5

tkt_21_ = (tvv_21_ / tqv_21_) 
print ("Media de Ticket do dia 21/01: ", tkt_21_)

media_periodo = (tkt_19_ + tkt_20_ + tkt_21_) / 3

print ("Media de Ticket do Período 19 á  21:",((media_periodo)))