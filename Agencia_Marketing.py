# # ATIVIDADE:

# CRIE UM BANCO DE DADOS PARA UMA AGENCIA DE MARKETING 

# PRECISA  CADASTRAR OS LEADS DA AGENCIA:

# DADOS: 

# NOME 

# IDADE

# EMAIL 

# ENDEREÇO

# TRABALHO

# GRADUÇÃO 

# APLIQUE TODAS DAS TRANSAÇÕES: 

# CITADAS ACIMA:

# tempo de atividade 45 minutos.


import sqlite3

conn = sqlite3.connect('Marketing.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
               id INTEGER RIMARY KEY,
               Nome TEXT NOT NULL,
               Idade INTERGIR NO NULL,
               Email TEXT NOT NULL,
               Endereço TEXT NOT NULL,
               Trabalho TEXT NOT NULL,
               Graduação TEXT NOT NULL
               )''')


nome = input('Digite seu nome ')
idade = int(input('Digite a sua Idade'))
email = input('Digite o seu email ')
endereço = input('Digite seu endereço ')
trabalho = input('Digite seu trabalho')
graduação = input('Digite sua graduação ')

cursor.execute('''
        INSERT INTO clientes (Nome, Idade, Email, Endereço, Trabalho, Graduação )
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, idade, email, endereço, trabalho, graduação,))

conn.commit()

cursor.execute('SELECT * FROM clientes ')
clientes = cursor.fetchall()

for clientes in clientes:
    print (f''' ID: {clientes[0]}, nome : {clientes[1]}, idade : {clientes[2]}, email : {clientes[3]}, endereço : {clientes[4]},
           trabalho : {clientes[5]}, graduação : {clientes[6]}
''')
    
conn.close()




#=====================================================================

#cod para grafico


import sqlite3
import tkinter as tk
from tkinter import messagebox





def conexao():
    conn =  sqlite3.connect('database.db')
    return conn


def criar_table():
    conex = conexao()
    c = conex.cursor()
    
    c.execute('''
      CREATE TABLE IF NOT EXISTS dados(
          cpf TEXT NOT NULL,
          email TEXT NOT NULL,
          nome TEXT NOT NULL            
        )''')
    conex.commit()
    conex.close()

def inserir_dados():
    nome  =  nome_input.get()
    cpf = CPF_input.get()
    email = email_input.get()

    if nome and cpf and email:
       conex = conexao()
       c = conex.cursor()
       c.execute('INSERT INTO dados (cpf, email, nome)values(?,?,?)', (cpf,email,nome))
       conex.commit()
       conex.close()
       messagebox.showinfo('Show', 'DADOS INSERIDOS COM SUCESSO!')
       nome_input.delete(0,tk.END)
       email_input.delete(0,tk.END)
       CPF_input.delete(0,tk.END)    
        
    else:
        messagebox.showerror('erro',  'Preencha os dados corretamente!!')






root =  tk.Tk()

nome_label = tk.Label(root, text='Nome', font = (70))
nome_label.pack()

nome_input = tk.Entry(root, font=70)
nome_input.pack()

CPF_label = tk.Label(root, text='CPF', font = (70))
CPF_label.pack()

CPF_input = tk.Entry(root, font=70)
CPF_input.pack()

email_label = tk.Label(root, text='E - mail', font = (70))
email_label.pack()

email_input = tk.Entry(root, font=70)
email_input.pack()


btn = tk.Button(root,text='Criar_Tabela', command=criar_table, width=30)
btn.pack(pady=20)

btn_inserir_ = tk.Button(root,text='iNSERIR DADOS', command=inserir_dados, width=30)
btn_inserir_.pack(pady=20)



root.mainloop()

#==========================================================

import sqlite3
import tkinter as tk
from tkinter import messagebox


def conexao():
    conn =  sqlite3.connect('database.db')
    return conn


def criar_table():
    conex = conexao()
    c = conex.cursor()
    
    c.execute('''
      CREATE TABLE IF NOT EXISTS dados(
          cpf TEXT NOT NULL,
          email TEXT NOT NULL,
          nome TEXT NOT NULL            
        )''')
    conex.commit()
    conex.close()


# inserindo os dados 
def inserir_dados():
    # capturando do input do tkinter 
    # atribuindo a variaveis locais 
    nome  =  nome_input.get()
    cpf = CPF_input.get()
    email = email_input.get()

    # se existir todos os inputs
    if nome and cpf and email:
       conex = conexao()
       c = conex.cursor()
       c.execute('INSERT INTO dados (cpf, email, nome)values(?,?,?)', (cpf,email,nome))
       conex.commit()
       conex.close()
       # enquanto não clicar na caixa de mensagem não apaga
       messagebox.showinfo('Show', 'DADOS INSERIDOS COM SUCESSO!')
       # apaga os valores iseridos na tabela
       nome_input.delete(0,tk.END)
       email_input.delete(0,tk.END)
       CPF_input.delete(0,tk.END)    
        
    else:
        # caso um dos inputs não estejam preenchidos 
        messagebox.showerror('erro',  'Preencha os dados corretamente!!')






root =  tk.Tk()

nome_label = tk.Label(root, text='Nome', font = (70))
nome_label.pack()

nome_input = tk.Entry(root, font=70)
nome_input.pack()

CPF_label = tk.Label(root, text='CPF', font = (70))
CPF_label.pack()

CPF_input = tk.Entry(root, font=70)
CPF_input.pack()

email_label = tk.Label(root, text='E - mail', font = (70))
email_label.pack()

email_input = tk.Entry(root, font=70)
email_input.pack()


btn = tk.Button(root,text='Criar_Tabela', command=criar_table, width=30)
btn.pack(pady=20)

btn_inserir_ = tk.Button(root,text='iNSERIR DADOS', command=inserir_dados, width=30)
btn_inserir_.pack(pady=20)


root.mainloop()
