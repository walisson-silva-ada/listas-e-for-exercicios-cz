def principal():
    dados_clientes = []
    menu = '1'
    
    while menu > '0':
        print("_________________________________")
        print("\n  ..:: MENU  PRINCIPAL ::...   ")
        print("_________________________________\n")
        print("Escolha uma opção:")
        print("1 - Cadastrar novo cliente")
        print("2 - Busca cliente pelo CPF")
        print("3 - Listar todos os clientes cadastrados")
        print("0 - Sair do sistema")
        menu = input("")
        
        if   menu == '1': dados_clientes = cadastra_cliente(dados_clientes)
        elif menu == '2': busca = busca_cliente(dados_clientes)
        elif menu == '3': listagem = lista_clientes(dados_clientes)
        elif menu == '0': print("Sistema finalizado!")
        else: print("Opção inválida!")

def cadastra_cliente(dados_clientes):
    
    print("_________________________________")
    print("\n     CADASTRO DE CLIENTE       ")
    print("_________________________________")
        
    nome  = input("Digite o nome do cliente:").capitalize()
    cpf = input("Digite o CPF do cliente:")
    #verifica se o CPF é valido
    validacao_cpf = valida_cpf(cpf)
    
    while validacao_cpf == False:
        cpf = input("Digite o CPF do cliente:")
        validacao_cpf = valida_cpf(cpf)
    
    email = input("Digite o e-mail do cliente:").lower()

    dados_clientes.append([nome,cpf,email])
    print("\n==============>> CLIENTE CADASTRADO COM SUCESSO!\n")
    return dados_clientes

def busca_cliente(dados_clientes):
    
    if len(dados_clientes) > 0:
        print("_________________________________")
        print("\n        BUSCA CLIENTE          ")
        print("_________________________________")
        busca_cpf = input("Digite o CPF para a busca: ")
        for i in range(len(dados_clientes)):
            if busca_cpf == dados_clientes[i][1]:
                return print(f"\nCliente: {dados_clientes[i][0]}\nCPF: {dados_clientes[i][1]}\ne-mail: {dados_clientes[i][2]}")
    else:
        return print("\n==============>> Não há clientes cadastrados")
     
    return print("\n==============>> Cliente não encontrado!")

def lista_clientes(dados_clientes):
    
    if len(dados_clientes) > 0:
        print("_________________________________")
        print("\n    LISTAGEM DE CLIENTES       ")
        print("_________________________________")
        for i in range(len(dados_clientes)):
            print(f"\nCliente: {dados_clientes[i][0]}\nCPF: {dados_clientes[i][1]}\ne-mail: {dados_clientes[i][2]}\n")
    else:
        return print("\n==============>> Não há clientes cadastrados")
        
def valida_cpf(cpf):
    lista_cpf = list(cpf)
    digito_cpf = lista_cpf[9:11]
    lista_cpf = lista_cpf[0:9]
    #lista auxiliar para calculo dos digitos
    lista_aux = []
    #multiplicador de 10 até 2 para cada digito
    mult1 = 10
    #multiplicador de 11 até 2 para cada digito incluindo o primeiro digito calculado
    mult2 = 11

    #9 primeiros digitos
    for i in range(9):
        primeiro_digito = int(lista_cpf[i])*mult1
        lista_aux.append(primeiro_digito)
        mult1 = mult1 - 1

    #calculo do primeiro digito segundo regra
    primeiro_digito = (sum(lista_aux)*10)%11

    #tratamento para calculo de digitos que tiveram como retorno >=10
    if primeiro_digito >= 10:
        digito_maior_10 = list(str(primeiro_digito))
        primeiro_digito = digito_maior_10[-1]

    lista_aux = []

    #for para implementar multiplicação pelo multiplicador segundo regra,
    #9 primeiros digitos + primeiro digito calculado
    for i in range(10):
        if i==9:lista_cpf.append(primeiro_digito)
        segundo_digito = int(lista_cpf[i])*mult2
        lista_aux.append(segundo_digito)
        mult2 = mult2 - 1

    #calculo do primeiro digito segundo regra
    segundo_digito = (sum(lista_aux)*10)%11

    if segundo_digito >= 10:
        digito_maior_10 = list(str(segundo_digito))
        segundo_digito = digito_maior_10[-1]

    #validação do digito
    if int(primeiro_digito) == int(digito_cpf[0]) and int(segundo_digito) == int(digito_cpf[1]):
        return True
    else:
        print("\n==============>> O CPF informado é inválido!")
    
    return False
        
principal()          