import random
import time




def aleatorio(n1,n2):
    return random.randint(n1,n2)


def _3_aleatorios(n1,n2):


    a = random.randrange(n1,n2)
    b = random.randrange(n1,n2)
    c = random.randrange(n1,n2)


    return a,b,c
      
def numeros_3(n1,n2,n3):

    a = random.randrange(n1)
    b = random.randrange(n2)
    c = random.randrange(n3)

    return a,b,c 

def contagem_regressiva():

    for contagem in (10, 0, -1):
        print(contagem)
        time.sleep(1)
    print("Fogo!") 

def numeros_pares(n1):
   if n1 < 2:
    return 0
   
   return sum(range(2, n1 + 1, 2))

numero = int(input("Digite um número inteiro positivo: "))
resultado = numeros_pares(numero)
print (f'A soma dos números pares de 2 até {numero} é {resultado}')

def tabuada (a):
   for n in range(1,10):
      resultado = n * a
      print (n, 'x',a,'=',resultado)
      return resultado
   


def contagem_regressiva_impares():
    """Exibe números ímpares de 99 a 1 em ordem decrescente."""
    for i in range(99, 0, -2):
        print(i)
   