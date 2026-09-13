# Sistema de Cadastro e Gerenciamento de Clientes em Python

def exibir_menu():
    print("\n" + "="*30)
    print("    SISTEMA DE CADASTRO")
    print("="*30)
    print("1. Cadastrar Novo Cliente")
    print("2. Listar Clientes")
    print("3. Buscar Cliente por E-mail")
    print("4. Sair")
    print("="*30)

def cadastrar_cliente(clientes):
    print("\n--- CADASTRO DE CLIENTE ---")
    nome = input("Nome completo: ").strip()
    email = input("E-mail: ").strip().lower()
    
    for cliente in clientes:
        if cliente["email"] == email:
            print("Erro: Já existe um cliente cadastrado com este e-mail.")
            return

    telefone = input("Telefone: ").strip()
    
    clientes.append({
        "nome": nome,
        "email": email,
        "telefone": telefone
    })
    print(f"Cliente '{nome}' cadastrado com sucesso!")

def listar_clientes(clientes):
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("Nenhum cliente cadastrado até o momento.")
        return
    
    for i, c in enumerate(clientes, 1):
        print(f"{i}. Nome: {c['nome']} | E-mail: {c['email']} | Tel: {c['telefone']}")

def buscar_cliente(clientes):
    print("\n--- BUSCAR CLIENTE ---")
    if not clientes:
        print("Nenhum cliente para buscar.")
        return
        
    busca = input("Digite o e-mail do cliente: ").strip().lower()
    encontrado = False
    
    for c in clientes:
        if c["email"] == busca:
            print(f"\n Cliente Encontrado:")
            print(f"Nome: {c['nome']}\nE-mail: {c['email']}\nTelefone: {c['telefone']}")
            encontrado = True
            break
            
    if not encontrado:
        print("Nenhum cliente encontrado com esse e-mail.")

def main():
    clientes = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            buscar_cliente(clientes)
        elif opcao == "4":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
