from PacoteArquivo.arquivo_csv import ArquivoCSV # Importando PacoteArquivo.arquivo_csv
from PacoteArquivo.arquivo_txt import ArquivoTXT # Importando PacoteArquivo.arquivo_txt

arquivo_banco_pacote = ArquivoCSV('banco.csv') # Instanciando a classe ArquivoCSV
arquivo_noticia_pacote = ArquivoTXT('noticia.txt') # Instanciando a classe ArquivoTXT

# Extraindo coluna education
education = arquivo_banco_pacote.extrair_colunas(indice_coluna=3) # Extraindo a coluna education
print(education)

titulo = arquivo_noticia_pacote.extrair_linha(numero_linha=1) # Extraindo a linha 1
print(titulo)