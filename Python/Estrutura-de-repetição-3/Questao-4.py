##4- Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo.
#Faça um programa que receba o código e o valor de 15 transações. Calcule e mostre: 
#O valor total das compras à vista,
#O valor total as compras a prazo,
#O valor total das compras efetuadas,
#O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes.

cAVista = 0
cAPrazo = 0
pComAPrazo = 0

for i in range (15):
    cod = int(input("Digite o código da transação (1/2): "))
    valor = float(input("Digite o valor da transação: "))

    if cod == 1:
        cAVista = cAVista + valor
    elif cod == 2:
        if cAPrazo == 0:
            pComAPrazo = valor            
        cAPrazo = cAPrazo + valor
    else:
        print("Erro. Digite um código válido.")
    
vTotal = cAPrazo + cAVista
v1Pres = pComAPrazo / 3

print("\nTotal das compras à vista: ", cAVista)
print("Total das compras à prazo: ", cAPrazo)
print("Total das compras: ", vTotal)
print("Valor da primeira das três prestações: ", v1Pres)  