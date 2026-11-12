#1-Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive) 
n = 0

for i in range (80): #aqui eu estou dizendo para i repetir 80 vezes
    num = float(input("Digite um número: "))

    if num >= 10 and num <= 150: #aqui eu estou dizendo para selecionar números maiores e igual a 10 e numeros menores e igual a 150
        n += 1 #qnd selecionar, adicionar na variavel n

print("Tem ",n," números dentro do intervalo.") 