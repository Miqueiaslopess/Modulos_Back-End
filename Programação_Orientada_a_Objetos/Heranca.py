from time import sleep
print ('------------------ Herança ------------------')
#------------------ Class Pessoa ------------------
class Pessoa(object):
    def __init__(self, nome: str, idade: int, cpf: str = None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def dormir(self,horas: int) -> None:
        for hora in range(1,horas+1):
            print(f'Dormindo por {hora} horas')
            sleep(1)
        
    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'Nome: {self.nome}\nIdade: {self.idade} anos\nCPF: {self.cpf}'
    
class Universidade(object):
    def __init__(self, nome:str):
        self.nome = nome
        
    
class Estudante(Pessoa):
    
    def __init__(self, nome:str,idade: int, cpf: str, universidade: Universidade):
        
        super().__init__(nome=nome, idade=idade, cpf=cpf)
        self.universidade = universidade

#------------------ Objetos ------------------
usp = Universidade(nome='Universidade de São Paulo')
miqueias = Estudante(nome='Miqueias Lopes', idade=20, cpf='123', universidade=usp)

#------------------ Manipulação ------------------
print(miqueias)
print(miqueias.universidade.nome)
