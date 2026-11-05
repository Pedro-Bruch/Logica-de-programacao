#7-	Crie um programa que solicite números ao usuário continuamente até que ele insira um número negativo.
#  Em seguida, exiba a média dos números positivos fornecidos.

num = 1
numTotal = 0
i = 0

while num > 0:
    num = int(input("Escreva um número: "))
    if num > 0:
        numTotal = num + numTotal
        i += 1
media = numTotal / i
print("A média dos números pares é: ", media)