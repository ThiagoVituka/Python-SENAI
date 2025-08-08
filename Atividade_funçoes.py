# ## Exercícios com funções:

# variáveis locais, globais e parâmetros

# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

# def verificar_numero ():

#     num = int(input('Digite um numero:  '))

#     if  num %2 ==0:
#         print ('O numero não e par')
#     else:
#         print ('O número e impar.')


# verificar_numero()


# ***2***

# ***CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

# def numero_multiplicação ():

#     nu1 = int(input('Digite um numero: '))
#     nu2 = int(input('Digite um numero: '))
#     nu3 = int(input('Digite um numero: '))

#     multi1 = nu1 * 3
#     multi2 = nu2 * 3
#     multi3 = nu3 * 3

#     print (multi1)
#     print (multi2)
#     print (multi3)

     

    
# numero_multiplicação()


# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# numero = int(input('Digite um numero: '))

# def numero_elevado(num):
#     exporente = (int(input('Digite um numero elevado ')))
#     calculo = num ** exporente
#     return calculo

# print  (numero_elevado(numero))


# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 
# 18 ANOS.***

# numero = int(input('Digite um número : '))

# def Mens_personal (num):
    
#     if numero == (18):
#         print ('Parabens você chegou a maioridade ')
#     else:
#         print('Não chegou a sua vez !!!')
    
    
# print (Mens_personal(numero))


# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

# def desco_idade(ano,ano_nasc):
#     c = ano - ano_nasc
#     print (c)

# desco_idade(2025,2000)



# ***6***

# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***


# def descobrir(ano,lista):
#     if ano in lista:
#         print ('Neste ano o Brasil ganhou')
#     else:
#         print ('O Brasil perdeu ')

# # anos = [1994, 1958, 1962, 1970, 2002]
# # descobrir(1999, anos)


# # ***7*** 

# # ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, 
# # MACARRONADA, SANDUICHE, SORVETE.***

# def restaurante():
#     menu = ['salada, Macarronada, Sanduiche, Sorverte']
#     print ('menu', menu)

#     pedido = input('Deseja pedir ??')
#     while pedido == "S":
#         escolhas = int(input('''
#         Menu :
#         1 SALADA
#         2 MACARRONADA
#         3 SANDUICHE
#         4 SORVETE
                                                          
# '''))
#     meus_pro.append(menu[escolhas])
#     pedido = input("Deseja algo mais ?")


# restaurante()





# ======================================

# correção 


# meus_pro = []
# def restaurante():
#     menu = ['','SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
#     print('menu', menu)
    
#     pedido = input('Deseja pedir? ')
#     while pedido ==  's':
#         escolhas  =  int(input('''
#          MENU:                       
#          1 SALADA
#          2 MACARRONADA
#          3 SANDUICHE
#          4 SORVETE     '''))                                    
                             


#         meus_pro.append(menu[escolhas]) 
#         pedido = input('Deseja algo mais? ')
#         print(meus_pro)
#     else: 
#         print('Obrigada volte sempre! ')

# restaurante()