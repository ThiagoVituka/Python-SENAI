# - ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar 
# um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*



# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*
 
# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***




#produto = input('Digite o tipo do quarto')

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.


# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

#qtd_dias = []
#quarto = [Hotel[secao1][produto]]




# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente.*

# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

# ***O sistema não deve usar loops (for, while) nem funções.**
# O código deve considerar todos os casos possíveis de escolha dos clientes.*


nome = input('Digite seu nome :')
idade = input('Digite a sua idade : ')


Hotel = {

      
        'Simples': 100.00,
        'Duplo' : 150.00,
        'Luxo' : 250.00 
       
    
}
Quarto = input('Digite o tipo do Quarto : ')
print(Hotel[Quarto])
Dias = int(input('Quantidade de dias : '))
valores = Dias * Hotel[Quarto]

print(valores)