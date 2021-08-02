cpf = input("Digite o CPF sem pontuação: ")
lista_cpf = list(cpf)
#dividindo o cpf em 2 listas para validação
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
    print(f"CPF válido!! Dígito verificador: {primeiro_digito}{segundo_digito}")
else:
    print("CPF INVÁLIDO!!")