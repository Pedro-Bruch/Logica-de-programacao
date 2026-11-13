#1- Faça um programa em Py que receba o total das vendas de cada vendedor e armazenadas em um vetor.
#Receba também o percentual de comissão de cada vendedor e armazene-os em outro vetor. 
#Receba os nomes desses vendedores e armazene ­os em um terceiro vetor. 
#Existem apenas dez vendedores. Calcule e mostre: 
#a) Um relatório com os nomes dos vendedores e os valores a receber; 
#b) O total das vendas de todos os vendedores; 
#c) O maior valor a receber e quem o receberá; 
#d) O menor valor a receber e quem o receberá.

vendas = []
comissao = []
nomes = []
totalVendasFull = 0
nomeMaior = ''
maior = 0
nomeMenor = ''
menor = None
totalVendedor = 10

for i in range(totalVendedor):
    nomeVendedor = input("Digite o nome do vendedor: ")
    totalVendas = float(input(f"Digite o total de vendas do vendedor {nomeVendedor}: "))
    percenComissao = float(input(f"Digite o percentual de comissao do vendedor {nomeVendedor}(sem %): "))
    print("\n")
    nomes.append(nomeVendedor)
    vendas.append(totalVendas)
    totalVendasFull += totalVendas
    
    valorComissao = totalVendas * (percenComissao/100)
    comissao.append(valorComissao)    
    
    if i == 0:
        maior = valorComissao
        nomeMaior = nomeVendedor
        menor = valorComissao
        nomeMenor = nomeVendedor
    else:       
        if valorComissao > maior:
            maior = valorComissao
            nomeMaior = nomeVendedor
            
        if valorComissao < menor:
            menor = valorComissao
            nomeMenor = nomeVendedor
        
   
print("----------------------")
print("       Relátorio       ")
for i in range(totalVendedor):
    print("Nome: ", nomes[i])
    print(f"Valor a receber: {comissao[i]}.")

print("----------------------")
print("O total de vendas dos funcionários foi: R$", totalVendasFull)
print("----------------------")
print(f"O maior valor pertence à {nomeMaior}, que foi de: R$ {maior} ")
print(f"O menor valor pertence à {nomeMenor}, que foi de: R$ {menor} ")