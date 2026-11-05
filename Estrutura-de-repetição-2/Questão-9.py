# Uma loja tem 150 clientes cadastrados e deseja mandar uma correspondência a cada um deles anunciando um bônus especial. 
# Escreva um algoritmo que leia o nome do cliente e o valor das suas compras no ano passado e calcule um bônus de 10% 
# se o valor das compras for menor que 500.000 e de 15 %, caso contrário.

for i in range (150):
    nome = input("\nDigite o nome do cliente: ")
    valor = float(input("Digite o valor das compras do ano passado: "))

    if valor < 500000:
        print("O bônus do ",nome," foi de: ", (valor * 0.1))
        
    else:
        print("O bônus do ",nome," foi de: ", (valor * 0.15))
    