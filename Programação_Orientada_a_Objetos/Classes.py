print('------------------ Classes ------------------')

#------------------ Atributos ------------------
from time import sleep

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