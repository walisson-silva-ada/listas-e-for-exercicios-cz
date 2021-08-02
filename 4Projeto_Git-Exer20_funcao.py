import random
baralho=[]
dicionario={}

def iniciar_jogo():
    count=1
    participantes=int(input('Informe o número de participantes:'))
    while count<=participantes:
        nome=str(input('Nome do jogador:'))
        dicionario[nome]=0
        count=count+1
    return dicionario

def criar_baralho():
    baralho=['a',2,3,4,5,6,7,8,9,10,'j','q','k']
    return baralho

def jogar(nome):
    pontuacao=dicionario[nome]
    if pontuacao==21:
        return 'Você ganhou!'
    
    if pontuacao>21:
        proximo=print('você não pode mais jogar!')
        return proximo
    
    else:
        sua_vez=str(input('Quer comprar uma nova carta(sim ou não)?'))
        return sua_vez

def sorteio(baralho):
    sortear=random.choice(baralho)
    if sortear=='a':
        print(sortear)
        pontuacao=dicionario[nome]
        pontuacao=pontuacao+1
        dicionario[nome]=pontuacao
        return dicionario
        
    elif type(sortear)==str:
        print(sortear)
        pontuacao=dicionario[nome]
        pontuacao=pontuacao+10
        dicionario[nome]=pontuacao
        return dicionario
        
    else: 
        print(sortear)
        pontuacao=dicionario[nome]
        pontuacao=pontuacao+sortear
        dicionario[nome]=pontuacao
        return dicionario
        
def verificar(dicionario):
    for chave in dicionario:
        pontuacao=dicionario[nome]
        if pontuacao>21:
            return print('{} sua pontuação é {} e é superior a 21!'.format(chave,pontuacao))
        
        elif pontuacao==21:
            return print('{} sua pontuação é {} e é igual à  21,você ganho!'.format(chave,pontuacao))
            
        else:
            return print('{} sua pontuação é {} e é inferior a 21!'.format(chave,pontuacao))

print('BlackJack')
print('Regra:Não passar de 21 pontos')
comecar=str(input('Vamos começar(sim ou não)?'))


if comecar=='sim':
    dicionario=iniciar_jogo()
    baralho=criar_baralho()
    print('Jogadores registrados:',dicionario)
    print('Baralho:',baralho)
    
    for chave in dicionario:
        nome=chave
        jogo=jogar(nome)
        while jogo=='sim':
                dicionario=sorteio(baralho)
                print(dicionario)
                jogo=jogar(nome)
                dicionario=sorteio(baralho)
                print(dicionario)
                verificar(dicionario)
                   
        else:
            print('Fim do jogo!')
            

else:
    print('Fim do jogo!')