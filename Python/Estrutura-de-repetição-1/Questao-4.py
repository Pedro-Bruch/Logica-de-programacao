#4-	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o número de filhos e salário. 
#A prefeitura deseja saber:   
#a) média do salário da população; 
#b) média do número de filhos; 
#c) maior salário; 
#d) percentual de pessoas com salário até R$100,00. 
#O final da leitura de dados se dará com a entrada de um salário negativo.

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