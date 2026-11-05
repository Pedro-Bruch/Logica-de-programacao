#5-	Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares. 
# Termine a leitura se o usuário digitar zero (0).

num = 1
contador = 0
numTotal = 0

while num != 0:
    num = int(input("Digite um número: "))
    if num % 2 == 0 and num != 0:
        contador += 1
        numTotal = num + numTotal    

media = numTotal / contador
print("A média dos números é: ", media)