#8-	Peça ao usuário um número inteiro positivo e exiba todos os números pares de forma decrescente até chegar a zero. 
# O programa deve exibir a sequência de forma organizada, considerando que o número de entrada pode ser par ou ímpar.

num = int(input("Digite um número inteiro positivo: "))

for i in range (num, -1, -1):
    if i % 2 == 0:
        print(i)