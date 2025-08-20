import tkinter as tk




def display():
    texto = input_.get()
    mostra_text.config(text=texto)





janela  =  tk.Tk()
janela.geometry('600x600')
janela.title('DISPLAY TEXT')


# pack() # grid() # place()

# Nome
# Idade
# E-mail
# Endereço
# Celular

# while True:
#     print("\n=== NOVO CADASTRO ===")
#     nome = input("Digite o nome: ")
#     idade = input("Digite a idade: ")
#     email = input("Digite o e-mail: ")



texto = tk.Label(janela, text ='Cadastro', background='blue', font=('Lao UI', 30), fg="white")
texto.grid(pady=0)


tk.Label(janela, text='Nome').grid(row=5)
tk.Label(janela, text='Idade').grid(row=6)
tk.Label(janela, text='E-mail').grid(row=7)
tk.Label(janela, text='Endereço').grid(row=8)
tk.Label(janela, text='Celular').grid(row=9)

e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e3 = tk.Entry(janela)
e4 = tk.Entry(janela)
e5 = tk.Entry(janela)
e1.grid(row=5, column=1)
e2.grid(row=6, column=1)
e3.grid(row=7, column=1)
e4.grid(row=8, column=1)
e5.grid(row=9, column=1)


btn = tk.Button(janela, text='Enviar', font=(25), fg='white', bg='black', command=display)
btn.grid(pady=20)

tk.mainloop()


# texto = tk.Label(janela, text ='Isso é um texto', background='BLUE', font=('Lao UI', 30), fg="white")
# texto.pack(pady=5)



# input_ = tk.Entry(janela,  font=(30), fg='purple')
# input_.pack(pady=30)



# btn = tk.Button(janela, text='Mostre o texto', font=(25), fg='white', bg='black', command=display)
# btn.pack(pady=20)



# mostra_text = tk.Label(janela, text='')
# mostra_text.pack(pady=20)




# janela.mainloop()