nome_aluno = input("Qual é o nome do aluno?")
idade = input("Qual é a idade do aluno?")
qtde_provas = int(input("Quantas provas ele fez?"))
lista_geral = []
lista_notas = []

while qtde_provas < 2:
    qtde_provas = int(input("Número de provas tem que ser maior que 2: "))

for i in range(qtde_provas):
    nota = input(f"Digite a {i+1}ª nota: ")
    lista_notas.append(float(nota))

lista_notas2 = list(lista_notas) 
lista_notas2.remove(max(lista_notas))
lista_notas2.remove(min(lista_notas))

avalia = False
if sum(lista_notas)/qtde_provas > 5:avalia = True
    
lista_geral.append(nome_aluno)
lista_geral.append(idade)
lista_geral.append(lista_notas)
lista_geral.append(lista_notas2)
lista_geral.append(sum(lista_notas)/qtde_provas)
lista_geral.append(sum(lista_notas2)/(qtde_provas-2))
lista_geral.append(avalia)

print("Lista com os dados do aluno:",lista_geral)