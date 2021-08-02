dicionario={}
num=10

def cadastro(num):

        cpf = str(input("Digite o CPF "))
        nome = str(input("Digite o nome "))
        email = str(input("Digite o email"))
        dicionario_cad={'nome':nome,'cpf':cpf,'email':email}
        dicionario[cpf]=dicionario_cad
        return print(dicionario)

def buscar(lista,cpf):
    
    if cpf in lista:
        return print('CPF encontrado!',lista[cpf])
    else:
        return print('CPF não encontrado!')
        

while num!=0:
    num=int(input("O que deseja fazer: (1)-Cadastrar,(2)-Buscar,(3)-Verificar cadastros,(0)-Finalizar consulta?"))
    if num==1:
        cadastro(num)
    elif num==2:
        cpf = str(input("Digite o CPF do usuario "))
        buscar(dicionario,cpf)
    elif num==3:
        print(dicionario)
    else:
        print('Finalizado!')
print('Obrigada!')
