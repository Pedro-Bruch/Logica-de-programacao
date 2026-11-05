#1-Feita uma pesquisa em 12 cidades para coletar dados sobre acidentes de
#trânsito. Foram obtidos os seguintes dados:
#- código da cidade
#- número de veículos de passeio
#- número de acidentes de trânsito com vítimas
#Código Cidade
#11 Jaraguá do Sul
#12 Joinville
#13 Blumenau
#14 Florianópolis
#21 Porto Alegre
#22 Bento Gonçalves
#23 Garibaldi
#24 Caxias do Sul
#31 Curitiba
#32 Foz do Iguaçu
#33 Toledo
#34 Cascavel
#Código Estado
#1 SC
#2 RS
#3 PR
#Deseja-se saber:
#a) o maior e o menor índice de acidentes de trânsito e a que cidades/estado
#pertencem
#b) qual a média de veículos nas cidades brasileiras (total / por estado)
#c) qual a média de acidentes com vítimas nas cidades de Santa Catarina e o
#total por estado.

i = 0
maior = 0
maiorNome = " "
menor = float('inf')
menorNome = " "
mediaVeiculo = 0
mediaAcidenteSc = 0
contadorSc = 0
totalAcidentes = 0 
mediaPr = 0
mediaRs = 0
mediaSc = 0

for i in range (12):
        cdd = int(input("Digite o código da cidade:\n11-Jaraguá do Sul | 12-Joinville | 13-Blumenau | 14-Florianópolis\n21-Porto Alegre | 22-Bento Gonçalves | 23-Garibaldi | 24-Caxias do Sul\n31-Curitiba | 32 Foz do Iguaçu | 33 Toledo | 34 Cascavel\n"))
        numVeiculo = int(input("Digite o número de veículos de passeio: "))
        numAcidente = int(input("Digite o número de acidentes de trânsito com vítimas: ")) 

        if cdd == 11:
                nome_cidade = "Jaraguá do Sul (SC)"
        elif cdd == 12:
                nome_cidade = "Joinville (SC)"
        elif cdd == 13:
                nome_cidade = "Blumenau (SC)"
        elif cdd == 14:
                nome_cidade = "Florianópolis (SC)"
        elif cdd == 21:
                nome_cidade = "Porto Alegre (RS)"
        elif cdd == 22:
                nome_cidade = "Bento Gonçalves (RS)"
        elif cdd == 23:
                nome_cidade = "Garibaldi (RS)"
        elif cdd == 24:
                nome_cidade = "Caxias do Sul (RS)"
        elif cdd == 31:
                nome_cidade = "Curitiba (PR)"
        elif cdd == 32:
                nome_cidade = "Foz do Iguaçu (PR)"
        elif cdd == 33:
                nome_cidade = "Toledo (PR)"
        elif cdd == 34:
                nome_cidade = "Cascavel (PR)"
        
        if numAcidente > maior:
                maior = numAcidente
                maiorNome = nome_cidade
        elif numAcidente > menor:
                menor = numAcidente
                menorNome = nome_cidade

        mediaVeiculo = mediaVeiculo + numVeiculo

        if cdd == 11 or cdd == 12 or cdd == 13 or cdd == 14:
                mediaAcidenteSc = mediaAcidenteSc + numAcidente
                mediaSc = numAcidente + mediaSc
                contadorSc += 1
        elif cdd == 21 or cdd == 22 or cdd == 23 or cdd == 24:
                mediaPr = numAcidente + mediaPr
        elif cdd == 31 or cdd == 32 or cdd == 33 or cdd == 34:
                mediaRs = numAcidente + mediaRs
        
mediaTotal = mediaVeiculo / 3
mediasSc = mediaAcidenteSc / contadorSc

print("O maior índice de acidentes de transito: ",maior," e pertence a ",maiorNome,)
print("O menor índice de acidentes de transito: ",menor," e pertence a ",menorNome,)
print("A média de veículos nas cidades brasileiras é: ",mediaTotal)
print("A média de acidentes de Santa Catarina é: ",mediasSc)
print("E o total de Santa Catarina é: ",mediaSc,", o total do Paraná é: ",mediaPr," e o total do Rio Grande do Sul: ",mediaRs)  