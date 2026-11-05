#6-Faça uma Programa que receba, como entrada, uma lista de números positivos ou negativos finalizada com o número zero e forneça,
#como saída, a soma dos números positivos, a soma dos números negativos e a soma das
#duas somas parciais e mostre os números pares e ímpares ao final.
num = 1
somaNegativo = 0
somaPositivo = 0
impar = []
par = []

while num != 0:
    num = int(input("Digite um número (Digite 0 para encerrar): "))

    if num < 0:
        somaNegativo = somaNegativo + num
    else:
        somaPositivo = somaPositivo + num
    
    if num % 2 == 0 and num != 0:
        par.append(num)
    elif num != 0:
        impar.append(num)

soma = somaPositivo + somaNegativo
    
print("Soma dos números positivos: ",somaPositivo)
print("Soma dos números negativos: ",somaNegativo)
print("Soma das duas parciais: ",soma)
print("Números Pares: ",par)
print("Números Impares: ",impar)