#10-	Solicite ao usuário um número inteiro n e exiba uma estrutura em forma de triângulo numérico de tamanho n. 
#Cada linha do triângulo deve conter números de 1 até o número da linha. Exemplo para 
#n = 5:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

n = int(input("Digite um número: "))
resultado = ""

for i in range (0, n):
    resultado += str(i + 1) + " "
    print(resultado)        