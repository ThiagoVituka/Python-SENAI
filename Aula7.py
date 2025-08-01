#e_comerce = {'Livro':['a','b']}

e_comerce = {

'livros':{
'a':10,
'b':20
},

'tablets':{
'a':20,
'b':10
},

'carnes':{
    'a':5,
    'b':2
},

'fones_de_ouvido':{
    'a':30,
    'b':15
}}

secao1 = input('Digite o seção 1')
secao2 = input('Digite o seção 2')

produto1 = input('Digite o produto 1')
produto2 = input('Digite o produto 2')


carrinho = [produto1, produto2]
valores =  [e_comerce[secao1][produto1],e_comerce[secao2][produto2]]
soma =  sum(valores)

print(carrinho)
print('R$', soma)

# #e_comerce = int(input(1))
# print(e_comerce.items('carnes'))