nota4 = 0
c4 = 0
c1 = 0
c3 = 0

for i in range(40):
    nome = input("Digite o nome do cliente: ")
    nota = int(input("1-Péssimo\n2-Regular\n3-Bom\n4-Excelente\nDigite a nota do atendimento: "))
    idade = int(input("Digite a idade do cliente: "))

    if nota == 4:
        nota4 = nota4 + idade
        c4 += 1
    elif nota == 1:
        c1 += 1
    elif nota == 3:
        c3 += 1

porc = (c3 / 40) * 100
media = nota4 / c4

print("A média de idade dos clientes que avaliaram como 'excelente' foi de: ", media)
print("O total de clientes que avaliaram como 'péssimo' foi de: ", c1)
print("A porcentagem de clientes que avaliaram 'bom' é: ", porc)