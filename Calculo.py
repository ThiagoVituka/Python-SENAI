# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função principal para o fluxo do sistema
def sistema_notas():
    # Dados do professor
    usuario_correto = "professor"
    senha_correta = "senha123"
    tentativas = 0

    # Tentativas de login
    while tentativas < 3:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Acesso concedido!")
            break
        else:
            tentativas += 1
            print(f"Login falhou! Tentativas restantes: {3 - tentativas}")
    
    if tentativas == 3:
        print("Conta bloqueada!")
        return

    # Menu do sistema
    alunos = {}
    
    while True:
        print("\n--- Menu ---")
        print("1. Inserir notas")
        print("2. Exibir média")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do aluno: ")
            notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]  # Inserir 3 notas
            alunos[nome] = notas
        elif opcao == '2':
            nome = input("Nome do aluno para ver a média: ")
            if nome in alunos:
                media = calcular_media(alunos[nome])
                print(f"Média de {nome}: {media:.2f}")
            else:
                print("Aluno não encontrado.")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Iniciar o sistema
sistema_notas()