import sqlite3

conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
               id INTERGE    PRIMARY AUO INCREMENT NO NULL,
               nome TEXT NOT NULL,
               idade INTERGIR NO NULL,
               cidade TEXT OT NULL
               ''')

# Inserir dados na tabela

nome = input('Digie um nome')
idade = int(input('Digie sua idade'))
cidade = input ( 'Cidade ')
cursor.execute('''
               INSERT INTO pessoas (nome, idade, cidade)
               VALUES (?, ?, ?)
               ''', (nome, idade, cidade)
)

#Confirmar a transação 

conexao.commit()

# Consultar dados da tabela 

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

# Mostrar os dados consultados 

for pessoa in pessoas:
    print (f''' ID: {pessoa[0]}, Nome : {pessoa[1]}, Idade : {pessoa [2]}, Cidade: {pessoa[3]}''')
    
#Fechar a conexão 
conexao.close()



