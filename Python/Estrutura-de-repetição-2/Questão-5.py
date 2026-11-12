#5-Supondo que a população de um país A seja 90 milhões de habitantes, crescendo com uma taxa anual de 3.5 % e 
# que a população de um país B seja 140 milhões de habitantes, crescendo a uma taxa anual de 1 %. Faça
# um algoritmo que calcule e mostre quantos anos serão necessários para que a população do país 
# A ultrapasse a população do país B.

paisA = 90000000
paisB = 140000000
i = 0

while paisB > paisA:

    paisA = (paisA * 0.035)
    paisB = (paisB * 0.01)

    i += 1

print("Foi necessários ",i," anos para a população do país A ultrapassar o país B")
