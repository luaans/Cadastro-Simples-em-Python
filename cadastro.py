import os

#lista para guardar us usuários
usuarios = []

#estrutura while para fazer repetição
while True:
    print("Cadastro de usuários")
    print()
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuários")
    print("3 - Buscar Usuário")
    opcao = int(input("Digite o número da opção desejada: "))

    #Limpa a tela 
    os.system('cls')  

    if opcao == 1:
        while True:
            print("Cadastro")
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            idade = input("Digite sua idade: ")

            #salvando o usuários na lista
            usuarios.append({
                "nome": nome,
                "email": email,
                "idade": idade
            })
            
            print("Cadastro Realizado!")
            
            #pergunta para poder cadastrar um novo usuários
            op = input("Deseja cadastrar um novo usuário? s/n: ").lower()
            if op != 's':
           
                break
          
            
    elif opcao == 2:
        #verifica se a lista esta vazia ou não
        if usuarios:
            print("Listando usuários:")
            #peroceorre os usuários da lista e depois exibe eles 
            for u in usuarios:
                print(f"Nome: {u['nome']}")
                print(f"Email: {u['email']}")
                print(f"Idade: {u['idade']}")
                print("-------------------------")
        else:
            print("Não existem usuários cadastrados.")
        
        #voltar ao menu
        op = input("Deseja voltar para o menu? s/n: ").lower()
        if op != 's':
            break
        os.system('cls')  

    elif opcao == 3:
        #opcap para digitar o nome do usuario para relizar a busca
        nome_busca = input("Digite o nome do usuário para buscar: ")
        encontrado = False
        #perocerre toda a lista fazendo a busca e exibe o resultado
        for u in usuarios:
            if u['nome'].lower() == nome_busca.lower():
                print("Usuário encontrado:")
                print(f"Nome: {u['nome']}")
                print(f"Email: {u['email']}")
                print(f"Idade: {u['idade']}")
                encontrado = True
                break
        
        #if com a mensagem se nao for encontrado usuários
        if not encontrado:
            print()
            print("Usuário não encontrado.")
        
        print()
        input("Pressione Enter para voltar ao menu...")
        os.system('cls')

    #caso seja selecionado uma opção não existente no menuo sera exibido essa mensagem abaixo 
    else:
        print("Opção inválida.")
        input("Pressione Enter para tentar novamente...")



        


