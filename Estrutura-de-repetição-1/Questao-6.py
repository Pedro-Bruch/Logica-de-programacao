#Peça ao usuário para fornecer um número inicial e um intervalo. 
# Em seguida, faça uma contagem regressiva do número inicial até zero, decrementando pelo intervalo especifica

num = int(input("Diga um número: "))
intervalo = int(input("Diga o intervalo: "))

for i in range(num, -1, -intervalo):
    print(i)

if num % intervalo != 0:
        print(0)