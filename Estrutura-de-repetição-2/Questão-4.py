#4-Faça um algoritmo que leia vários códigos do jogador (1 ou 2) que ganhou o ponto em uma partida de pingue-pongue, 
# e responda quem ganha a partida. A partida chega ao final se um dos jogadores chega a 21 pontos e a
#diferença de pontos entre os jogadores é maior ou igual a dois. Caso contrário, ganha aquele que, 
# com mais de 21 pontos, consiga colocar uma vantagem de dois pontos sobre o adversário
import random
ponto1 = 0
ponto2 = 0

while True:
    
    print("=== PLACAR ===\n\nJogador 1 = ",ponto1,"\nJogador 2 = ",ponto2,"\n")
    
    ponto = random.randint(1, 2)      

    if ponto == 1:
        ponto1 += 1
    elif ponto == 2:
        ponto2 += 1
    else:
        print("Erro, digite um jogador válido.")

    if ponto1 >= 21 and ponto1 - ponto2 >= 2:
        print("Jogador 1 ganhou")
        break
    elif ponto2 >= 21 and ponto2 - ponto1 >= 2:
        print("Jogador 2 ganhou")
        break    