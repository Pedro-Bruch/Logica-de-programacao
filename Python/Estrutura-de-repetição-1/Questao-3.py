#3-	Fazer um programa que retorne quantos valores digitados pelo usuário são negativos. 
# Repetir o enquanto até o usuário digitar o valor ZERO:
valor = 1
contador = 0

while valor != 0:
    valor = float(input("Digite um valor:"))
    if valor < 0:
        contador += 1

print("Você digitou ", contador," números negativos.")  