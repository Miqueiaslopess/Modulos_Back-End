# Padrao Conjuntos: nome = {}
frutas = {'banana', 'maca','uva'}
print(frutas)
print(type(frutas))

#Paises da Americas
paises_america_sul = {'brasil', 'argentina', 'peru', 'eua'}
paises_america_norte = {'eua', 'canada', 'mexico'}
paises_america_central = {'costa rica', 'panamá'}

paises_america = paises_america_sul - paises_america_norte
print(paises_america)

paises_america = paises_america_norte - paises_america_sul
print(paises_america)

# --------------- Metodos --------------- #
areas_cursos = {'Exatas', 'Humanas', 'Biológicas'}
print(areas_cursos)

# inserir um elemento no cojunto: set.add(val)
areas_cursos.add('Saúde')
print(areas_cursos)

# remover um elemento no conjunto: set.remove(val)
areas_cursos.remove('Saúde')

# ----------------- Conversões ----------------- #  

# ----------------- Motivação ----------------- #  
hastags_seg = ['#tiago', '#joao', '#bbb']
hastags_ter = ['#sarah', '#bbb', '#fiuk']
hastags_qua = ['#gil', '#thelma', '#lourdes']
hastags_qui = ['#rafa', '#fora', '#danilo']
hastags_sex = ['#juliete', '#arthur', '#bbb']

hastags_semana = hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex
print(hastags_semana)

print(len(hastags_semana))
 
hastags_semana = list(set(hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex))
print(hastags_semana)
print(len(hastags_semana))