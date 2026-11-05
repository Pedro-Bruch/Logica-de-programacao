nota7 = 0
tNota = 0

for i in range (35):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    
    tNota = tNota + nota

    if nota > 7:
        nota7 += 1

media = tNota / 35

print("\nA média geral da turma é: ", media)
print("Nessa turma, teve ",nota7," pessoas acima de 7")