#2- Utilizando vetores, crie um programa que organize uma quantidade qualquer de números inteiros 
#fornecidos pelo usuário da seguinte forma: primeiro os números pares em ordem crescente e 
#depois os números ímpares em ordem decrescente. 

numeros = []
pares = []
impares = []
qntdNumeros = int(input("Digite a quantidade de números: "))

for i in range(qntdNumeros):
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort(reverse=True)

print(pares, impares)
    