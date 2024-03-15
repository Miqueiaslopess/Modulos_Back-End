# isalnum() - Retorna True se todos os caracteres na string são alfanuméricos
texto = "Python123"
eh_alfanumerico = texto.isalnum()
print("isalnum():", eh_alfanumerico)

# isalpha() - Retorna True se todos os caracteres na string estão no alfabeto
texto = "Python"
eh_alfabetico = texto.isalpha()
print("isalpha():", eh_alfabetico)

# isascii() - Retorna True se todos os caracteres na string são caracteres ASCII
texto = "Hello"
eh_ascii = texto.isascii()
print("isascii():", eh_ascii)

# isdecimal() - Retorna True se todos os caracteres na string são decimais
texto = "12345"
eh_decimal = texto.isdecimal()
print("isdecimal():", eh_decimal)

# isdigit() - Retorna True se todos os caracteres na string são dígitos
texto = "12345"
eh_digito = texto.isdigit()
print("isdigit():", eh_digito)

# isidentifier() - Retorna True se a string é um identificador válido
texto = "var_name"
eh_identificador = texto.isidentifier()
print("isidentifier():", eh_identificador)

# islower() - Retorna True se todos os caracteres na string estão em minúsculas
texto = "python"
eh_minusculo = texto.islower()
print("islower():", eh_minusculo)

# isnumeric() - Retorna True se todos os caracteres na string são numéricos
texto = "12345"
eh_numerico = texto.isnumeric()
print("isnumeric():", eh_numerico)

# isprintable() - Retorna True se todos os caracteres na string são imprimíveis
texto = "Hello\nWorld"
eh_imprimivel = texto.isprintable()
print("isprintable():", eh_imprimivel)

# isspace() - Retorna True se todos os caracteres na string são espaços em branco
texto = "    "
eh_espaco = texto.isspace()
print("isspace():", eh_espaco)

# istitle() - Retorna True se a string segue as regras de um título
texto = "Title Case Example"
eh_titulo = texto.istitle()
print("istitle():", eh_titulo)

# isupper() - Retorna True se todos os caracteres na string estão em maiúsculas
texto = "PYTHON"
eh_maiusculo = texto.isupper()
print("isupper():", eh_maiusculo)

# join() - Converte os elementos de um iterável em uma string
lista = ["Hello", "World"]
string_concatenada = " ".join(lista)
print("join():", string_concatenada)

# ljust() - Retorna uma versão justificada à esquerda da string
texto = "Python"
justificado_esquerda = texto.ljust(10)
print("ljust():", justificado_esquerda)

# lower() - Converte a string para minúsculas
texto = "Python"
minusculas = texto.lower()
print("lower():", minusculas)

# lstrip() - Retorna uma versão da string com espaços à esquerda removidos
texto = "    Python"
trim_esquerda = texto.lstrip()
print("lstrip():", trim_esquerda)

# maketrans() - Retorna uma tabela de tradução para ser usada em traduções
tabela = str.maketrans("aeiou", "12345")
texto = "python"
traduzido = texto.translate(tabela)
print("translate():", traduzido)

# partition() - Retorna uma tupla onde a string é dividida em três partes
texto = "Python Programming"
particionado = texto.partition(" ")
print("partition():", particionado)

# replace() - Retorna uma string onde um valor especificado é substituído por outro valor
texto = "Hello, World!"
substituido = texto.replace("World", "Python")
print("replace():", substituido)

# rfind() - Procura a string por um valor especificado e retorna a última posição onde foi encontrado
texto = "python programming"
ultima_posicao = texto.rfind("o")
print("rfind():", ultima_posicao)

# rindex() - Procura a string por um valor especificado e retorna a última posição onde foi encontrado
texto = "python programming"
ultima_posicao = texto.rindex("o")
print("rindex():", ultima_posicao)

# rjust() - Retorna uma versão justificada à direita da string
texto = "Python"
justificado_direita = texto.rjust(10)
print("rjust():", justificado_direita)

# rpartition() - Retorna uma tupla onde a string é dividida em três partes começando da direita
texto = "Python Programming"
particionado_direita = texto.rpartition(" ")
print("rpartition():", particionado_direita)

# rsplit() - Divide a string no separador especificado e retorna uma lista
texto = "Python Programming"
dividido_direita = texto.rsplit(" ")
print("rsplit():", dividido_direita)

# rstrip() - Retorna uma versão da string com espaços à direita removidos
texto = "Python    "
trim_direita = texto.rstrip()
print("rstrip():", trim_direita)

# split() - Divide a string no separador especificado e retorna uma lista
texto = "Python Programming"
dividido = texto.split(" ")
print("split():", dividido)

# splitlines() - Divide a string nas quebras de linha e retorna uma lista
texto = "Hello\nWorld"
linhas = texto.splitlines()
print("splitlines():", linhas)

# startswith() - Retorna True se a string começa com o valor especificado
texto = "Hello, World!"
comeca_com = texto.startswith("Hello")
print("startswith():", comeca_com)

# strip() - Retorna uma versão da string com espaços em branco removidos dos dois lados
texto = "    Python    "
trim_ambos = texto.strip()
print("strip():", trim_ambos)

# swapcase() - Inverte as maiúsculas para minúsculas e vice-versa
texto = "Python Programming"
invertido = texto.swapcase()
print("swapcase():", invertido)

# title() - Converte o primeiro caractere de cada palavra para maiúscula
texto = "python programming"
titulo = texto.title()
print("title():", titulo)

# translate() - Retorna uma string traduzida usando uma tabela de tradução
tabela = str.maketrans("aeiou", "12345")
texto = "python"
traduzido = texto.translate(tabela)
print("translate():", traduzido)

# upper() - Converte a string para maiúsculas
texto = "python"
maiusculas = texto.upper()
print("upper():", maiusculas)

# zfill() - Preenche a string com um número especificado de zeros à esquerda
texto = "35"
preenchido = texto.zfill(10)
print("zfill():", preenchido)

