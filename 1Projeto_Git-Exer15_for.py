nome=str(input('Nome do aluno:'))
idade=int(input('Idade do aluno:'))
quantidade_provas=int(input('Quantidade de provas que o aluno realizou:'))

lista=[]
lista_notas=[]

count=1

while count<=quantidade_provas:
    nota=float(input('Por favor, informe quais são as notas do aluno:'))
    lista_notas.append(nota)
    count=count+1
media=sum(lista_notas)/len(lista_notas)
teste=media>=5

lista.append(nome)
lista.append(idade)
lista.append(lista_notas)
lista.append(media)
lista.append(teste)
print(lista)