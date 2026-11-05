mAdmin = 0
cAdmin = 0
mOper = 0
cOper = 0

for i in range(20):
    cod = int(input("1-Admin\n2-Operacional\nDigite o código: "))
    salario = float(input("Digite o salário: "))

    if cod == 1:
        mAdmin = mAdmin + salario
        cAdmin += 1
    elif cod == 2:
        mOper = mOper + salario
        cOper += 1
    else:
        print("Erro. Digite um código válido.")

mediaAdmin = mAdmin / cAdmin
mediaOper = mOper / cOper
tSalario = mAdmin + mOper

print("A média salarial do setor administrativo é: ", mediaAdmin)
print("A média salarial do setor operacional é: ", mediaOper)
print("O total de salários pagos pela empresa foi de: R$",tSalario)
print("A quantidade de funcionários no setor Administrativo é: ",cAdmin)
print("A quantidade de funcionários no setor Operacional é: ",cOper)