# Title: Funções 02

def escreve_arquivo_csv(nome:str, cabecalho: str, conteudos: list) -> bool:
    try:
        with open(file=nome, mode='w', encoding='utf8') as fp:
            linha = cabecalho + '\n' # Escrevendo o cabeçalho
            fp.write(linha) # Escrevendo o cabeçalho
            for conteudo in conteudos: # Escrevendo o conteúdo
                linha = str(conteudo) + '\n' # Convertendo o conteúdo para string
                fp.write(linha) # Escrevendo o conteúdo
    except Exception as error: # Tratando exceções
        print(f'Erro: {error}') # Imprimindo o erro
        return False 
    return True 

# Testando a função
nome = 'idades-funcao.csv'
cabecalho = 'idade'
conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43] # Lista de idades

'''
# Simulando Erro
nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
conteudos = 10
'''

# Escrevendo o arquivo
escreveu_com_sucesso = escreve_arquivo_csv(nome=nome, cabecalho=cabecalho, conteudos=conteudos)
print(f'Escreveu com sucesso: {escreveu_com_sucesso}')