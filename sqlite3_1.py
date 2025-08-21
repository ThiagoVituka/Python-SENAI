# import sqlite3

# conexao = sqlite3.connect('meu_banco_de_dados.db')
# cursor = conexao.cursor()

# cursor.execute('''
#         CREATE TABLE IF NOT EXISTS pessoas (
#                id INTERGE    PRIMARY AUTO INCREMENT NO NULL,
#                nome TEXT NOT NULL,
#                idade INTERGIR NO NULL,
#                cidade TEXT OT NULL
#                ''')

# # Inserir dados na tabela

# nome = input('Digie um nome')
# idade = int(input('Digie sua idade'))
# cidade = input ( 'Cidade ')
# cursor.execute('''
#                INSERT INTO pessoas (nome, idade, cidade)
#                VALUES (?, ?, ?)
#                ''', (nome, idade, cidade)
# )

# #Confirmar a transação 

# conexao.commit()

# # Consultar dados da tabela 

# cursor.execute('SELECT * FROM pessoas')
# pessoas = cursor.fetchall()

# # Mostrar os dados consultados 

# for pessoa in pessoas:
#     print (f''' ID: {pessoa[0]}, Nome : {pessoa[1]}, Idade : {pessoa [2]}, Cidade: {pessoa[3]}''')
    
# #Fechar a conexão 
# conexao.close()

# importar a lib 
import sqlite3
# from tkinter import *



# criar o banco de dados
conexao = sqlite3.connect('banco.db')



# permitir usar o sql no arquivo python
c = conexao.cursor()


# criamos tabelas 


c.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
          
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
     nome TEXT NOT NULL,
     idade INTEGER NOT NULL,
     cidade TEXT NOT NULL            
    )
''')



nome =  input('Nomes: ')
idade =  int(input('Idade; '))
cidade = input('Cidade: ')


# inserindo dados na tebela


c.execute('''INSERT INTO pessoas(nome, idade, cidade)
          values (?,?,?)''',(nome, idade, cidade))



#  atualizar o documento
conexao.commit()



# seleção de toda tabela
c.execute('SELECT * FROM pessoas')
# torna um lista 
dados = c.fetchall()


# iterado a lista  -  percorrendo a lista
for dados_tabela in dados:
    print(f'id {dados_tabela[0],dados_tabela[1], dados_tabela[2], dados_tabela[3]}')


# fechando a conexão
conexao.close()    


