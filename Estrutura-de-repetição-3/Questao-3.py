#3-Faça um algoritmo que receba um número e mostre 
#uma mensagem caso este número seja  maior que 80, menor que 25 ou igual a 40. 

num = float(input("Digite um número: "))

if num > 80:
    print("Esse número é maior que 80")
elif num < 25:
    print("Esse número é menor que 25")
elif num == 40:
    print("Esse número é 40.")
else:
    print("Esse número é normal")