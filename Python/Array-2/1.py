#1- Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. No final, mostre:
#a) Qual é a média da turma
#b) Quantos alunos estão acima da média da turma 
#c) Qual foi a maior nota digitada
#d) Em que posições a maior nota aparece

notas = []
maior = 0
mediaNotas = 0
acimaMedia = 0
posicoesMaiores = []

for i in range(10):
    nota = float(input("Digite a nota do aluno: "))
    
    mediaNotas += nota
    if nota > maior:
        maior = nota
        
        
    notas.append(nota)

media = mediaNotas / 10

for i in range (10):
    posicao = notas[i]
    
    if posicao > media:
        acimaMedia += 1
    if posicao == maior:
        posicoesMaiores.append(i)

maiorNota = notas.index(maior)

print("A média da turma é: ", media)
print(acimaMedia," alunos estão acima da média da turma.")
print("A maior nota digitada foi: ",maior,".\nEla aparece na posição ",posicoesMaiores)

        

