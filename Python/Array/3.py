#3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 (121 dias)
#Não ocorreu temperatura inferior a 15ºC e nem superior a 40ºC. Fazer um programa python que determine: 
#a) A menor temperatura ocorrida 
#b) A maior temperatura ocorrida 
#c) A temperatura média do período

menor = None
maior = None
totalTemp = 0
diasValidos = 0

while diasValidos < 121:
    temp = float(input("Digite a temperatura do dia: "))
    
    if temp < 15 or temp > 40:
        continue
    
    if menor == None:
        maior = temp
        menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
            
    totalTemp += temp
    diasValidos += 1
media = totalTemp / diasValidos

print("A menor temperatura registrada foi: ",menor,"ºC")
print("A maior temperatura registrada foi: ",maior,"ºC")
print("A temperatura média foi: ",media)