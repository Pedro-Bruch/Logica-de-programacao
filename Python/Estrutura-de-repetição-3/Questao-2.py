#2 - Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher. 
#No final informe total de homens e de mulheres.

h = 0
m = 0

for i in range (56): #Aqui estou dizendo para repetir 56 vezes o que esta dentro do for
    nome = input("Digite seu nome: ")
    sexo = input("Qual o sexo? (h/m): ")

    if sexo == 'h': #aqui eu separo se é homem ou mulher, depois, somar a variavel h(homem) ou m(mulher)
        h += 1
        print(nome, " é homem.")
    elif sexo == 'm':
        m += 1
        print(nome, " é mulher.")
    else:
        print("Digite um sexo válido") #caso digite outra letra, da erro
        
    

print("No total, foi informado ",h," homens e ",m," mulheres") 