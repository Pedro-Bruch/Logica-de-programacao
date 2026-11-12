#9-	Crie um programa de adivinhação em que o computador escolhe aleatoriamente um número entre 1 e 50, 
# e o usuário precisa adivinhar. O programa deve fornecer feedback (maior ou menor) a cada 
# tentativa e permitir apenas 5 tentativas para acertar. 
# Se o usuário acertar antes do limite, exiba uma mensagem de vitória; 
# caso contrário, revele o número ao final.

import random
num = random.randint(1, 2)
print("O número sorteado foi: ", num)
for i in range (5):
    num2 = int(input("Digite um valor: "))
    if num2 == num:
        print("Acertou")
        break
    elif num > num2:
        print("Tente novamente, meu número é maior.")
    elif num < num2:
        print("Tente novamente, meu número é menor")
print("Suas tentativas acabaram. Meu número era: ", num)