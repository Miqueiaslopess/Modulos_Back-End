''' 1. Classe para ler arquivos de texto
Crie a classe ArquivoTexto. Ela deve conter os seguintes atributos:

self.arquivo: Atributo do tipo str com o nome do arquivo;
self.conteudo: Atributo do tipo list onde cada elemento é uma linha do arquivo;
A classe também deve conter o seguinte método:

self.extrair_linha: Método que recebe como parâmetro o número da linha e retorna o seu conteúdo.
'''
class ArquivoTexto(object):

    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = []

    def extrair_linha(self, numero_linha: int):
        return self.conteudo[numero_linha - 1]

    def ler_arquivo(self):
        with open(self.arquivo, 'r') as arquivo:
            self.conteudo = arquivo.readlines()

# Utilize o código abaixo para testar sua classe.
arquivo_texto = ArquivoTexto(arquivo='musica.txt')

numero_linha = 1
print(arquivo_texto.extrair_linha(numero_linha=numero_linha)) # Roda Viva

numero_linha = 10
print(arquivo_texto.extrair_linha(numero_linha=numero_linha)) # Mas eis que chega a roda viva

'''2. Classe para ler arquivos de csv
Crie a classe ArquivoCSV. Ela deve extender (herdar) a classe ArquivoTexto para reaproveitar os seus atributos (self.arquivo e self.conteudo) e método (self.extrair_linha). Além disso, adicione o seguinte atributo:

self.colunas: Atributo do tipo list onde os elementos são os nome das colunas;
A classe também deve conter o seguinte método:

self.extrair_coluna_da_linha: Método que recebe como parâmetro o numero da linha e o indice da coluna e retorna o valor em questão.
'''

class ArquivoCSV(ArquivoTexto):

    def __init__(self, arquivo: str):
        super().__init__(arquivo)
        self.colunas = []

    def extrair_coluna_da_linha(self, numero_linha: int, numero_coluna: int):
        linha = self.extrair_linha(numero_linha)
        coluna = linha.split(',')
        return coluna[numero_coluna - 1]

    def ler_arquivo(self):
        super().ler_arquivo()
        self.colunas = self.conteudo[0].split(',')
        self.conteudo = self.conteudo[1:]

arquivo_csv = ArquivoCSV('carros.csv')
arquivo_csv.ler_arquivo()

# Utilize o código abaixo para testar sua classe.
arquivo_csv = ArquivoCSV(arquivo='carros.csv')

numero_linha = 1
print(arquivo_csv.extrair_linha(numero_linha=numero_linha)) # id,valor_venda,valor_manutencao,portas,pessoas,porta_malas

print(arquivo_csv.colunas) # ['id', 'valor_venda', 'valor_manutencao', 'portas', 'pessoas', 'porta_malas']

numero_linha = 10
print(arquivo_csv.extrair_linha(numero_linha=numero_linha)) # 9,low,med,2,2,small

numero_linha = 10
numero_coluna = 2
print(arquivo_csv.extrair_coluna_da_linha(numero_linha=numero_linha, numero_coluna=numero_coluna)) # low