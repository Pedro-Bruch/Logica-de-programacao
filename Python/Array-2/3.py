#3- Faça um programa que leia e monte dois vetores de números inteiros com 20 números cada.
#Depois de montados, gere um terceiro vetor formado pela diferença dos dois vetores lidos, 
#um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto vetor 
#formado pela multiplicação dos dois vetores lidos.

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    vetor1.append(numero)  
    
for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    vetor2.append(numero)  
    
for i in range(20):
    num = vetor1[i] - vetor2[i]
    vetor3.append(num)
    
for i in range(20):
    num = vetor1[i] + vetor2[i]
    vetor4.append(num)
    
for i in range(20):
    num = vetor1[i] * vetor2[i]
    vetor5.append(num)
    
print("Vetor 1: ", vetor1)
print("Vetor 2: ", vetor2)
print("Vetor 3: ", vetor3)
print("Vetor 4: ", vetor4)
print("Vetor 5: ", vetor5)
