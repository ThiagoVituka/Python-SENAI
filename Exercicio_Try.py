# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira 
# algo que não seja um número inteiro.

# try:
#     numero = int(input('Digite um número inteiro: '))
#     print(f'O número inserido foi {numero}.')
# except ValueError:
#     print('Errp: Você não inseriu um número inteiro válido. ')




# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. 
# Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# a = int(input('Digite um número'))
# b = int(input('Digite um número'))

# try:
#       print(a/b)

# except ZeroDivisionError as error:
#       print(error)

# else:
#       print( ' Sem erros')

# finally:
#       print('Aqui sempre vai printar')

# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o parametro do 
# elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um 
# indice que não exista na lista).

def erros(numero):
    lista = [1,2,3,4,5]

    try:
          print(lista[numero])
    except IndexError:
          print('')



resultado 


# def exercicio(l):
#     try:
#        i = int(input('Digite um número: '))
#        print(l[i])
#     except IndexError as erro:
#        print(erro)
#     finally:
#        print('Fim de carregamento ...')   


# l = [1,2,3]
# exercicio(l)   



# def dv():
#    try: 
#     n1 = int(input('Numero: '))
#     n2 = int(input('Numero: '))


#     n1/n2
#    except ZeroDivisionError as erro:
#      print(erro)


# dv()      



def verificar():
    try:
        n = int(input('teste'))


    except ValueError as erro:
        print(erro)


verificar()