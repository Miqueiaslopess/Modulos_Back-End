class Vendedor():
    def __init__(self, nome: str):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas: int):
        self.vendas = vendas

    def bateu_meta(self, meta: 1000):
        if self.vendas >= meta:
            print(f'{self.nome} bateu a meta')
        else:
            print(f'{self.nome} não bateu a meta')

    def __str__(self) -> str:
        return f'---------- Vendedor {self.nome} ----------\nVendas: {self.vendas}'


vendedor1 = Vendedor(nome='Miqueias')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(1000)

vendedor2 = Vendedor(nome='Pedro')
vendedor2.vendeu(500)
vendedor2.bateu_meta(1000)

vendedor3 = Vendedor(nome='Maria')
vendedor3.vendeu(1500)
vendedor3.bateu_meta(1000)

print(vendedor1)
print(vendedor2)
print(vendedor3)
