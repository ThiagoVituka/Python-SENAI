# EXERCÍCIOS 1: 
# Utilize condicionais

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

# usuario = int(input('Digite um número '))

# if usuario >= 0:
#     print('O número e positivo')
# else:
#     print('O número e negativo ')


# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

# usuário = int(input('Didite a sua idade '))

# if usuário >= 18:
#     print ('Você está apto a votar !')
# else:
#     print ('Você é menor de idade não pode votar ! ')


# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

# numero = 10

# if numero % 2 == 0:
#     print ('O numero é par. ')
# else:
#     print ('O número é impar ')

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# n1 = float(input('Digite o primeiro lado1 '))
# n2 = float(input('Digite o segundo lado2 ')) 
# n3 = float(input('Digite o segundo lado3')) 

# if (n1 + n2 > n3)
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.

# 6*

# Verifique se um número é positivo e maior que 10

# 7*

# Verifique se um número é divisível por 3 ou 5.


# num =  int(input('NUmero: '))

# if num > 0:    print('Positivo')
# elif num < 0:    print('Negativo')
# else: print('Zero')        


# idade =  int(input('Idade: '))

# if idade > 16:
#     print('Pode votar')
# else:
#     print('Não pode')

# n = int(input('Numero: '))


# if n % 2 == 0:
#     print('Par')
# else:
#     print('Impar')    


# # equilátero, isósceles ou escaleno


# l1 = int(input('lado 1: '))
# l2 = int(input('lado 2: '))
# l3 = int(input('lado 3: '))

# if l1 == l2 == l3 == l1:
#     print('Equilatero')
# elif l1 != l2 != l3 != l1:
#     print('escaleno')   
# else:
#     print('isoceles')     


# n = int(input('Numero: '))

# if n % 5 == 0 and n % 7 == 0:
#     print('é divisivel por 5 e  7 ')
# else:
# #     print('Não é')    

# n = int(input('Numero: '))


# if n > 0 and n > 10:
#     print('Verdade')
# else:
#     print('Erro')    

n = int(input('Numero: '))

if n % 3 == 0 or n % 5 ==0:
    print('Verdade')
else:
    print('False')    