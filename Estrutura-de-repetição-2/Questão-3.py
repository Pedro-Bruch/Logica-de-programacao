#João tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano. 
# Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Zé seja maior que João.

joao = 150
ze = 110
i = 0

while ze <= joao:

    joao += 2
    ze += 3
    i += 1

print("Foi necessário ",i," anos para Zé ser mais alto que João.")
