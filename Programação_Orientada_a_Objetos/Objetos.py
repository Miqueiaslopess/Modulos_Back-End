print('------------------ Classes ------------------')

from time import sleep
#------------------ Atributos ------------------
class Pessoa(object):
    def __init__(self, nome: str, idade: int, cpf: str = None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas + 1):
            print(f'Dormindo por {hora} horas')
            sleep(1)
        
    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return (f'Nome: {self.nome}\nIdade: {self.idade} anos\nCPF: {self.cpf}')
    
#------------------ Objetos ------------------
miqueias = Pessoa(nome='Miqueias Lopes', idade=20, cpf='123')
maria = Pessoa(nome='Maria Martins', idade=81, cpf='456')
pedro = Pessoa(nome='Pedro Lopes', idade=25, cpf='789')

#------------------ Manipulação ------------------
print(miqueias.nome)

# ------------------ Função ------------------
def maior_de_idade(idade: int) -> bool:
    return idade >= 18

# ------------------ Verificando se é maior de idade ------------------
if maior_de_idade(idade=miqueias.idade):
    print(f'{miqueias.nome} é maior de idade')
else:
    print(f'{miqueias.nome} é menor de idade')

# ------------------ Função ------------------
score_credito = {'123': 1000, '456': 500, '789': 0}

def verificar_credito(cpf: str) -> int:
    return score_credito[cpf]

# ------------------ Metodo: Verificar Creditos dos Usuarios ------------------
print(verificar_credito(miqueias.cpf))
print(verificar_credito(maria.cpf))
print(verificar_credito(pedro.cpf))

# ------------------ Metodos ------------------
miqueias.dormir(1)
miqueias.falar('Olá, como vai?')
print(miqueias)
type(miqueias)