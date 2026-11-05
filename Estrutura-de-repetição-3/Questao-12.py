m3 = 0
somaPar = 0

for i in range(50):
    num = int(input("Digite um número: "))

    if num % 3 == 0:
        m3 += 1
    
    if num % 2 == 0:
        somaPar = somaPar + num

print("Nessa sequência de números tem ",m3," números múltiplos de 3.")
print("A soma dos números pares dessa sequência é de: ", somaPar)