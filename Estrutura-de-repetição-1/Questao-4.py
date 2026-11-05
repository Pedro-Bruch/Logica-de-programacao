
contador = 0
salarioTotal = 0
filhosTotal = 0
menorSalario = 0
maiorSalario = 0
salario = 1
while salario > 0:
    salario = float(input("Digite o salário: ")) 
    filho = int(input("Digite a quantidade de filhos: "))

    if salario > 0:
        salarioTotal = salario + salarioTotal
        filhosTotal = filho + filhosTotal
        contador += 1        

    if salario > maiorSalario:
        maiorSalario = salario

    if salario <= 100 and salario > 0:
        menorSalario += 1   

else: 
    media = salarioTotal / contador
    media2 = filhosTotal / contador
    media3 = (menorSalario / contador) * 100

    print("A média do salário da população é: ", media, "\nA média de número de filhos é: ", media2, "\nO maior salário é: ", maiorSalario, "\nO percentual de pessoas com salário menor que 100 é: ", media3)