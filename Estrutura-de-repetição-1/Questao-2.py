#2-	Fazer um programa que calcule a tabuada de qualquer número, e o limite de cálculo deve ser definido pelo usuário:

num = int(input("Digite o número: "))
tab = int(input("Até qual número deseja a tabuada?: "))

for contador in range (1, tab+1):
    print(num, " x ", contador, " = ", num * contador) 