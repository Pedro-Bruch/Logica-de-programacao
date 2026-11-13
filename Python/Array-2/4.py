#4-Em uma classe há n alunos, cada um dos quais realizou k provas com pesos distintos. 
#Dados n , k, os pesos das k provas e as notas de cada aluno, 
#calcular a média ponderada das provas para cada aluno e a média aritmética da classe em cada uma das provas

alunos = int(input("Número de alunos: "))
provas = int(input("Número de provas: "))

pesos = []
for i in range(provas):
    peso = float(input(f"Peso da prova {i+1}: "))
    pesos.append(peso)

soma_pesos = sum(pesos)
soma_notas_provas = [0] * provas

for i in range(alunos):
    print(f"\nNotas do Aluno {i+1}")
    soma_ponderada_aluno = 0.0    
    for j in range(provas):
        nota = float(input(f"Nota na prova {j+1}: "))
        soma_ponderada_aluno += nota * pesos[j]
        soma_notas_provas[j] += nota        
    media_aluno = soma_ponderada_aluno / soma_pesos
    print("Média ponderada do Aluno", i+1, media_aluno)

for j in range(provas):
    media_prova = soma_notas_provas[j] / alunos
    print("Média da Prova",j+1,":", media_prova)
