alunos = {
    'professor': 'senha123',
}


def calcular_media(notas):
    return sum(notas) / len(notas)

def sistema_notas():
    usuario_correto = 'professor'
    senha_correta = 'senha123'
    tentativas = 0 

    while tentativas <3:
        usuario = input ('Digite o nome de usuário :  ')
        senha = input('Digite a senha !  ')

        if usuario == usuario_correto and senha_correta:
            print ('Acesso liberado  ')
            
        else:
            tentativas +=1
            print("Login falhou ! Tentativas restantes : {3 - tentativas}")

    if tentativas ==3:
        print ('Conta Bloquada! ')


        

Alunos = {

    'Aluno1' : ('Digite a nota'),
    'Aluno2' : ('Digite a nota'),
    'Aluno3' : ('Digite a nota')
}


    










