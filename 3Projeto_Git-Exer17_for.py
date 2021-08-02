count=0

#Listas
lista_cpf=[]
lista_num=[]

lista=list(range(2,11))
lista_sorte=sorted(lista)[::-1]

lista1=list(range(2,12))
lista_sorte1=sorted(lista1)[::-1]

cpf=str(input('Informe os 11 digitos do seu cpf:'))

#str para lista
for i in range(len(cpf)):
    lista_cpf.append(cpf[i])

#lista em str para int
for letra in lista_cpf:
    num=int(letra)
    lista_num.append(num)
print('Número do CPF:',lista_num)

#Multiplicação dos elementos entre listas
x=[elementoSorte*elementoNum for elementoSorte,elementoNum in zip(lista_sorte,lista_num)]
x=sum(x)

#Verificação do digito
if (x*10%11 == lista_num[9]):
    y=[elementoSorte1*elementoNum for elementoSorte1,elementoNum in zip(lista_sorte1,lista_num)]
    y=sum(y)
    y*10%11 == lista_num[10]

print('Lista entre 10 a 2:',lista_sorte)
print('lista entre 11 a 2:',lista_sorte1)
print('Resultado para verificação do primeiro verificador:',x*10%11 == lista_num[9])
print('Resultado para verificação do segundo verificador:',y*10%11 == lista_num[10])