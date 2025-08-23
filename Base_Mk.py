import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# 2. SITUAÇÃO PROBLEMA: FORMULÁRIO DE LEADS PARA UMA AGENCIA DE

# MARKETING DIGITAL

# A AGÊNCIA "MARKETING DIGITAL" ESTÁ SEM UM SISTEMA ADEQUADO PARA

# GERENCIAR OS LEADS (POTENCIAIS CLIENTES) QUE RECEBE POR MEIO DE

# CAMPANHAS ONLINE. ATUALMENTE, OS LEADS SÃO ARMAZENADOS

# MANUALMENTE EM PLANILHAS, O QUE DIFICULTA O SEU GERENCIAMENTO E

# A RÁPIDA CONSULTA DOS DADOS. A AGÊNCIA PRECISA DE UM SISTEMA

# EFICIENTE PARA GERENCIAR E ACOMPANHAR OS LEADS.

# Solução proposta: Criar um formulário de cadastro de leads com campos

# como nome, e-mail, número de telefone e interesse no serviço. O sistema

# também permitirá visualizar, editar e excluir os leads, além de atualizar o

# status do lead (por exemplo, “Em andamento”, “Convertido”, “Perdido”).


#CREATE READ UPDATE DELETE



def conectar():
    conn = sqlite3.connect('Nova_Visao.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        contato INTEGER,
        servico TEXT NOT NULL
       )  
   ''')
    conn.commit()
    conn.close()

def inserir_usuarios():
    nome  = entry_nome.get()
    email = entry_email.get()
    contato = entry_contato.get()
    servico = entry_servico.get()
    

    if nome and servico:
        conn = conectar()
        c = conn.cursor()    
        c.execute('INSERT INTO usuarios (nome, email, contato, servico ) VALUES (?,?,?,?) ', (nome, email, contato, servico))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Dados inseridos!')
        entry_nome.delete(0,tk.END)
        entry_email.delete(0,tk.END)
        entry_contato.delete(0,tk.END)
        entry_servico.delete(0,tk.END)
        mostrar_usuarios()
    else:
        messagebox.showerror('Erro','Preencha corretamente!')    

def mostrar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios  =  c.fetchall()
    for usuario in usuarios:
        tree.insert("","end", values = (usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
    conn.close()        


def eliminar_():
    selecao = tree.selection()
    if selecao:
        user_id = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ? ', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Efetuado', 'Dados deletados!')
        mostrar_usuarios()
    else:
        messagebox.showinfo('Erro', 'Selecione corretamente')    

def atualizar():
    selecao = tree.selection()
    if selecao:
       user_id = tree.item(selecao)['values'] [0]
       nome  = entry_nome.get()
       email = entry_email.get()
       contato = entry_contato.get()
       servico = entry_servico.get()


       if nome and email:
          conn = conectar()
          c = conn.cursor()    
          c.execute('UPDATE usuarios SET  nome = ?, email = ? contato = ? servico = ? WHERE id = ?',(nome, email, contato, servico, user_id))
          conn.commit()
          conn.close()
          messagebox.showinfo('Dados', 'Atualização funcionou!')
          mostrar_usuarios()
       else:
           messagebox.showerror('Erro', 'Dados não foram atualizados!') 
    else:
        messagebox.showwarning('Atenção', 'Selecione corretamente') 




janela = tk.Tk()
janela.title('CRUD COM TKINTER E SQLITE 3')
# janela.geometry('500x860')

label_nome = tk.Label(janela, text = 'Nome', font=(30))
label_nome.grid()

entry_nome = tk.Entry(janela, font=(30))
entry_nome.grid()


label_email = tk.Label(janela, text = 'email', font=(30))
label_email.grid()

entry_email = tk.Entry(janela, font=(30))
entry_email.grid()

label_contato = tk.Label(janela, text = 'contato', font=(30))
label_contato.grid()

entry_contato = tk.Entry(janela, font=(30))
entry_contato.grid()


label_servico = tk.Label(janela, text = 'servico', font=(30))
label_servico.grid()

entry_servico = tk.Entry(janela, font=(30))
entry_servico.grid()

# entry_id = tk.Entry(janela, font=(30))
# entry_id.grid()


btn_salvar = tk.Button(janela, text='salvar', font=(30), command=inserir_usuarios)
btn_salvar.grid()

btn_deletar = tk.Button(janela, text='deletar', font=(60), command=eliminar_)
btn_deletar.grid()

btn_atualizar = tk.Button(janela, text='atualizar', font=(90), command=atualizar)
btn_atualizar.grid()



collumns = ('ID', 'NOME', 'E-mail', 'CONTATO', 'SERVICO')



texto = tk.Label(janela, text ='Cadastro', background='blue', font=('Lao UI', 30), fg="white")
texto.grid(pady=0)






# btn = tk.Button(janela, text='Enviar', font=(25), fg='white', bg='black', command=display)
# btn.grid

tree = ttk.Treeview(janela, columns= collumns, show='headings')
tree.grid(row=20, column=10, columnspan=3)

for col in collumns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuarios()


janela.mainloop()