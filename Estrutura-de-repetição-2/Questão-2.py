#2-Construa um algoritmo que receba o código de vários produtos e os
#classifique de acordo com a tabela:
#CÓDIGO CLASSIFICAÇÃO
#1 Alimento não-perecível
#2 a 4 Alimento perecível
#5 e 6 Vestuário
#7 Higiene pessoal
#8 a 15 Limpeza e utensílios domésticos
#Qualquer outro código inválido exibe uma mensagem ao usuário.
#Quando o usuário digitar 0 (zero) o programa finaliza e exibe o número total
#de produtos classificados em cada categoria.

nPerecivel = 0 #1
perecivel = 0 #2a4
vestuario = 0 #5e6
hPessoal = 0 #7
limEutenDomes = 0 #8a15
num = 1

while num != 0:
    num = int(input("Digite o código do produto (Digite 0 para parar): "))
    
    if num == 1:
        nPerecivel += 1
    elif num > 1 and num <= 4:
        perecivel += 1
    elif num >= 5 and num <= 6:
        vestuario += 1
    elif num == 7:
        hPessoal += 1
    elif num > 7 and num <= 15:
        limEutenDomes += 1
    else: 
        print("Erro. Digite um código válido!")

print("\n=== PRODUTOS CADASTRADOS ===\n")
print("Não Perecível = ",nPerecivel)
print("Perecível = ",perecivel)
print("Vestuário = ",vestuario)
print("Higiene Pessoal = ",hPessoal})
print("Limpeza e utensílios domésticos = ",limEutenDomes)
