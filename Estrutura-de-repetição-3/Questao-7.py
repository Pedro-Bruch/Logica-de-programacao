#Cachorro Quente     100      R$ 1,20
#Bauru Simples       101      R$ 1,30
#Bauru com ovo       102      R$ 1,50
#Hambúrguer          103      R$ 1,20
#Cheeseburguer       104      R$ 1,30
#Refrigerante        105      R$ 1,00

ped = 1
vTotal = 0

while ped != 0:
    print("\n===========  CARDÁPIO   ===========\n")
    print("Cachorro Quente --- 100 --- R$ 1,20")
    print("Bauru Simples ----- 101 --- R$ 1,30")
    print("Bauru com ovo ----- 102 --- R$ 1,50")
    print("Hambúrguer -------- 103 --- R$ 1,20")
    print("Cheeseburguer ----- 104 --- R$ 1,30")
    print("Refrigerante ------ 105 --- R$ 1,00\n")
    print("Total: R$", vTotal ,"\n")
    ped = int(input("Digite o código do produto(0 para encerrar): "))

    if ped == 0:
        break

    qntd = int(input("Digite a quantidade desse produto: "))

    if ped == 100:
        vTotal = (qntd * 1.20) + vTotal
    elif ped == 101:
        vTotal = (qntd * 1.30) + vTotal
    elif ped == 102:
        vTotal = (qntd * 1.50) + vTotal
    elif ped == 103:
        vTotal = (qntd * 1.20) + vTotal
    elif ped == 104:
        vTotal = (qntd * 1.30) + vTotal
    elif ped == 105:
        vTotal = (qntd * 1) + vTotal
    else:
        print("Digite um código válido.")

print("Total à pagar: R$", vTotal)

