##5- Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: 
#ótimo=3, bom=2, regular=1. 
#Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre: (2 pontos)
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados

iMedia = 0
regular = 0
bom = 0
c = 0
medias = 0

for i in range (15):
    idade = int(input("Digite sua idade: "))
    opn = int(input("Qual sua opnião do filme?\n3-Ótimo\n2-Bom\n1-Regular\n"))
    
    if opn == 3:
        iMedia = iMedia + idade
        medias += 1
        c += 1
    elif opn == 1:
        regular += 1
        c += 1
    elif opn == 2:
        bom += 1
        c += 1
    else:
        print("Coloque uma opnião válida.")

media = iMedia / medias
porc = (bom / c) * 100

print("\nA média das pessoas que responderam ótimo é: ", media)
print("A quantidade de pessoas que responderam regular é: ", regular)
print("A porcentagem de pessoas que responderam bom é: ", porc "%")

    
    

   
    

