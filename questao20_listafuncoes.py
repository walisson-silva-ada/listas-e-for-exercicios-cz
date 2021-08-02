import random as rd

def principal():
    dados_jogadores = []
    
    print("_______________________________________________")
    print("\n            B L A C K   J A C K                ")
    print("_______________________________________________\n")
    print("START...\n\n")
    
    qtde_jogadores = int(input("Quantos jogadores temos? "))
    
    
    
    for i in range(qtde_jogadores): 
        nome = input(f"Qual é o nome do {i+1}º jogador? ").capitalize()
        #iniciando todas as info dos jogadores, pontos = 0 e ativo
        dados_jogadores.append([nome,0,'ativo'])

    baralho = cria_baralho()
    
    for i in range(len(dados_jogadores)):
        print("\n================================================")
        print(f"\n >>>>> VEZ DE {dados_jogadores[i][0].upper()} <<<<< ")
        jogada = cria_jogada(dados_jogadores[i])
    
    print("\n===============================================")
    print("\nO jogo acabou!\n")
    
    vencedor, max_pontos = verifica_placar(dados_jogadores)
    
    print("_______________________________________________")
    if max_pontos > 0:
        print(f"\nO VENCEDOR É... << {vencedor.upper()} >>> PARABÉNS!")
    else:
        print("\nNão há vencedor nessa rodada!")
    print("_______________________________________________")

def cria_baralho():
    baralho = []
    [baralho.append(i) for i in range(14) if i > 0]
    return baralho
    
def cria_jogada(dados_jogador):
    jogada = input(f"{dados_jogador[0]}, deseja comprar uma carta? S ou N ").upper()
    
    if dados_jogador[2] == 'ativo':
        while jogada == 'S':
            carta, pontos, txtcarta = sorteia_carta(cria_baralho())
            dados_jogador[1] = dados_jogador[1] + pontos
            print(f"==========>> Você tirou a carta {txtcarta} e agora tem {dados_jogador[1]} pontos\n")
            if dados_jogador[1] < 21:
                jogada = input(f"{dados_jogador[0]}, deseja comprar mais uma carta? S ou N ").upper()
            else:
                print("Você não pode mais comprar pois tem 21 ou mais pontos")
                break

    dados_jogador[2] = 'inativo'
    return(dados_jogador)

def sorteia_carta(baralho):
    pontos = 0
    carta = rd.randint(baralho[0],baralho[-1])
    txtcarta = ''

    if carta in range(11,14):
        pontos = 10
    else:
        pontos = carta
    
    if carta == 1: txtcarta = "Ás"
    elif carta == 11: txtcarta = "Dama"
    elif carta == 12: txtcarta = "Valete"
    elif carta == 13: txtcarta = "Rei"
    else: txtcarta = carta
    
    return carta, pontos, txtcarta

def verifica_placar(dados_jogadores):
    max_pontos = 0
    dono_max_pontos = ' '
    
    print("_______________________________________________")
    print("\n  ..:: R E S U L T A D O   P L A C A R ::..")
    print("_______________________________________________")
    
    for i in range(len(dados_jogadores)):
        if max_pontos < dados_jogadores[i][1] and dados_jogadores[i][1] <= 21:
            max_pontos = dados_jogadores[i][1]
            dono_max_pontos = dados_jogadores[i][0]
            
        print(f"\nJogador: {dados_jogadores[i][0]}\n >>> Pontos: {dados_jogadores[i][1]}")
    
    return dono_max_pontos, max_pontos

principal()