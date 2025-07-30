# lista  =  [1,20,31,45,50,61]
# lista[1] = 200
# print(lista)


# soma  =  lista[2] + lista[-1]
# print(soma)


# isso_e_uma_lista = list(range(1,251,2))
# print(isso_e_uma_lista)


# l = list(range(1,11))
# print(l)


# funções:


# funções para adicionar um dado
l = []
print(l)
l.append(10)
print(l)
l.extend([10,1,2,0])
l +=(5,332,65)
l.insert(0,250)
l[0] = 250
print(l)


# deleta o último valor
l.pop(1)
l.remove(250)
del l[3]
print(l)


# print(dir(l))

# lista  =  [1,20,31,45,50,61]
# lista[1] = 200
# print(lista)


# soma  =  lista[2] + lista[-1]
# print(soma)


# isso_e_uma_lista = list(range(1,251,2))
# print(isso_e_uma_lista)


# l = list(range(1,11))
# print(l)


# funções:


# funções para adicionar um dado
l = []
print(l)
l.append(10)
print(l)
l.extend([10,1,2,0])
l +=(5,332,65)
l.insert(0,250)
l[0] = 250
print(l)


# deleta o último valor
# l.pop(1)
l.remove(250)
# del l[3]
print(l)


# print(dir(l))


# funlções que nã i impactam s estrutura da lista. 
print(len(l))
print(max(l))
l.sort(reverse=True)
print(l)





# Multiplique 4 por 6 e divida o resultado por 2. (Concatene com a palavra resultado)

resultado =  (4*6)/2
print('Resultado', resultado)



# Calcule a soma de 5 e 7.(Concatene com a palavra 
# resultado)
n1 = 5
n2 = 7
print( 'Resultado',n1 + n2)

# Eleve 3 à potência de 4.(Concatene com a 
# palavra resultado)

potencia  =  3 ** 4
print('Resultado', potencia)


# Calcule a média de 8, 12 e 15.(Concatene com 
# a palavra resultado)

lista  =  [8,12,15]

media  = sum(lista)/len(lista)
print('Resultado', media)


# Subtraia 10 de 2 e multiplique o resultado por 
# 5.(Concatene com a palavra resultado)

sub = 10 - 2
mult =  sub * 5

m = (10 - 2) * 5
print('Resultado', mult)

# Divida 27 por 3 e some 5.
# (Concatene com a palavra resultado)


r =  27 / 3  + 5
print('Resulta', r)

# Exercícios com variáveis / print() / input()(opcional):

# Calcule o módulo ( % ) de 17 por 4.

modulo = 17 % 4
print(modulo)

# Multiplique 9 por 3 e, em seguida, 
# eleve o resultado ao quadrado.

multiplicacaO = (9 * 3) ** 2

print('Resultado', multiplicacaO)

# Calcule a raiz quadrada de 81.

raiz  =  81 ** 0.5
print('Resultado', raiz)

# Adicione 20 a 3 vezes 4.

calculo =  3 * 4 + 20
print(calculo)

# Multiplique 15 por 2 e, em seguida, subtraia 7.

mul = 15 * 2 - 7
print(mul)

# Eleve 5 ao cubo.

cubo =  5 ** 3
print(cubo)

# Calcule a média de 17, 21 e 25.

media2  =  17 + 21 + 25
r = media2/3
print(r)


# Multiplique 11 por 2 e adicione 7.

m =  11 * 2 + 7
print(m)

# Subtraia 15 de 3 vezes 8 e divida o resultado por 2.

sub =  ((3*8) -15)/2
print(sub)

# Eleve 2 à potência de 10.

potencia  =  2 ** 10

print(potencia)


#+++++++++++++++++++++++++++++++++++++++++++++++++

# Média  de alunos


lista_nomes = []
lista_aluno1 = []
lista_aluno2 = []
lista_aluno3 = []
lista_medias = []

aluno1, aluno2 , aluno3 = input('Nome: '),input('Nome: '),input('Nome: ')
lista_nomes.extend([aluno1,aluno2, aluno3])


n1 =float(input(f'Nota 1 aluno(a) {aluno1}: '))
n2 = float(input(f'Nota 2 aluno(a) {aluno1}: '))
n3 = float(input(f'Nota 3 aluno(a) {aluno1}: '))

n4 =float(input(f'Nota 1 aluno(a) {aluno2}: '))
n5 = float(input(f'Nota 2 aluno(a){aluno2}:'))
n6 = float(input(f'Nota 3 aluno(a) {aluno2}: '))

n7 =float(input(f'Nota 1 aluno(a) {aluno3}: '))
n8 = float(input(f'Nota 2 aluno(a){aluno3}: '))
n9 = float(input(f'Nota 3 aluno(a){aluno3}: '))

lista_aluno1 += (n1,n2,n3)
lista_aluno2 +=  (n4,n5,n6)
lista_aluno3 += (n7,n8,n9)

# notas de cada aluno: 
print(lista_nomes[0], 'Notas', aluno1)
print(lista_nomes[1], 'Notas', aluno2)
print(lista_nomes[2], 'Notas', aluno3)

media1 = sum(lista_aluno1)/len(lista_aluno1)
media2 = sum(lista_aluno2)/len(lista_aluno2)
media3 = sum(lista_aluno3)/len(lista_aluno3)





lista_medias.extend([media1, media2, media3])

print(f'''
aluno:                  |   media
{lista_nomes[0]}        |   {lista_medias[0]}
{lista_nomes[1]}        |   {lista_medias[1]}
{lista_nomes[2]}        |   {lista_medias[2]}



''')

maior = max(lista_medias)
indice = lista_medias.index(maior)

# qual a maior média
print('Maior média', max(lista_medias))

# Aluno com a maior médio
print('O aluno que tirou a maior média dia foi o', lista_nomes[indice])