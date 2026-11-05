#12, 18, 24, 30, 36, 42, 48, 54 e 60.
pCarro = float(input("Digite o valor do carro: "))
fPagamento = input("Deseja pagar à vista?(y/n): ")

if fPagamento == 'y':
    print("Preço à vista: R$ ", pCarro - (pCarro * 0.2))
elif fPagamento == 'n':
    print("\n=== PARCELAS ===\n")
    print("6 parcelas =\nValor Final: R$ ",(pCarro * 0.03)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.03)+ pCarro)/6, "\n")
    print("12 parcelas =\nValor Final: R$ ",(pCarro * 0.06)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.06)+ pCarro)/12, "\n")
    print("18 parcelas =\nValor Final: R$ ",(pCarro * 0.09)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.09)+ pCarro)/18, "\n")
    print("24 parcelas =\nValor Final: R$ ",(pCarro * 0.12)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.12)+ pCarro)/24, "\n")
    print("30 parcelas =\nValor Final: R$ ",(pCarro * 0.15)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.15)+ pCarro)/30, "\n")
    print("36 parcelas =\nValor Final: R$ ",(pCarro * 0.18)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.18)+ pCarro)/36, "\n")
    print("42 parcelas =\nValor Final: R$ ",(pCarro * 0.21)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.21)+ pCarro)/42, "\n")
    print("48 parcelas =\nValor Final: R$ ",(pCarro * 0.24)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.24)+ pCarro)/48, "\n")
    print("54 parcelas =\nValor Final: R$ ",(pCarro * 0.27)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.27)+ pCarro)/54, "\n")
    print("60 parcelas =\nValor Final: R$ ",(pCarro * 0.3)+ pCarro, "\nValor Parcela: R$ ", ((pCarro * 0.3)+ pCarro)/60, "\n")

    parcela = int(input("\nEm quantas vezes deseja fazer?: ")) 
    if parcela >= 6 and parcela <= 60 and parcela % 6 == 0:
        print("Compra realizada")
    else:
        print("Digite uma parcela válida.")
else:
    print("Digite uma letra válida.")    


