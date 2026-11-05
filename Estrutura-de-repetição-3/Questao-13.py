#13-Simulação de Crescimento Populacional com Evento Crítico
#Duas populações A e B crescem anualmente:
#A cresce 3% ao ano
#B cresce 1,5% ao ano
#A cada 5 anos ocorre uma crise que reduz ambas em 7%.
#Determine em quantos anos A ultrapassa B, considerando valores iniciais informados pelo usuário.

popA = float(input("Digite a população do país A: "))
popB = float(input("Digite a população do país B: "))
i = 0

while popA < popB:
    popA = popA + (popA*0.03)
    popB = popB + (popB*0.015)

    if i % 5 == 0:
        popA = popA - (popA*0.07)
        popB = popB - (popB*0.07)

    i +=1

print("O país A demorou ",i," anos para ultrapassar o país B." )