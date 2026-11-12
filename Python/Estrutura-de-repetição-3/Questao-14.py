##14-Entrada contínua de temperaturas.
#Regras:
#Ignorar valores < -50 ou > 150
#Encerrar com 999
#Contar temperaturas:
#Entre 20 e 80
#Múltiplas de 5
#Que não sejam divisíveis por 10
#Exibir:
#Quantidade válida
#Maior temperatura válida
#Percentual válido sobre total digitado

temp = 0
tempValida = 0
maior = 0
i = 1

while temp != 999:
    temp = float(input("Digite a temperatura(Digite 999 para encerrar): "))

    if temp > -50 and temp < 150:
        if temp > 20 and temp < 80 and temp % 5 == 0 and temp % 10 != 0:
            tempValida += 1
            if temp > maior:
                maior = temp
        
        i += 1

perc = (tempValida / i) * 100

print("\nQuantidade válida: ", tempValida)
print("Maior temperatura válida: ", maior, "ºC")
print("Percentual válido: ", perc,"%")
