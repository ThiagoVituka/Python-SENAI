def teste():
    try:
        n = int(input('Numero: '))
        z = int(input('Numero: '))


        n/z
        # print(n*5)
        # lista =  [1,3,4]
        # print(lista[6]) 
        # div = n /0
        # print(div)


    except ZeroDivisionError as erro:
        print(erro)
    except ValueError as erro:
        print(erro)    
    except TypeError as erro:
        print(erro)
    except SyntaxError as erro:
        print(erro)
    except IndexError as erro:
        print(erro)
    except IndentationError as erro:
        print(erro)
    except IndexError as erro:
        print(erro)                    
    else:
        print('erro desconhecido')  
    finally:
        print('Fim de carregamento...')        


teste()


