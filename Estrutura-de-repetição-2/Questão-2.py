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
