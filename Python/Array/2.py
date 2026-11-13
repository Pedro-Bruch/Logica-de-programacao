#2- Faça um programa em Py que leia um vetor de seis elementos numéricos inteiros, calcule e mostre: 
#a) A quantidade de números pares 
#b) Quais os números pares 
#c) A quantidade de números ímpares 
#d) Quais os números ímpares

numerosInteiros = []
pares = []
qntPares = 0
impares = []
qntImpares = 0

for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    numerosInteiros.append(numero)
    
    if numero % 2 == 0:
        qntPares += 1
        pares.append(numero)
    else:
        qntImpares += 1
        impares.append(numero)

print("------------------")
print(f"A quantidade de números pares foi: {qntPares}\nOs números pares digitados foi: {pares}")
print(f"A quantidade de números ímpares foi: {qntImpares}\nOs números ímpares digitados foi: {impares}")
    

