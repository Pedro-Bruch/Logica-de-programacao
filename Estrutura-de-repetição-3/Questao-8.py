#8 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
#valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Qtd parcelas	% Juros sobre o valor inicial da dívida
#1	0
#3	10
#6	15
#9	20
#12	25
#Saída do programa
#Valor da Dívida - Valor dos Juros - Qtd de Parcelas - Valor da Parcela 
#R$ 1.000 0 1 R$ 1.000,00 
#R$ 1.100 100 3 R$ 366,00 
#R$ 1.150 150 6 R$ 191,67

dvd = float(input("Digite o valor da dívida: "))
print("VALOR DA DÍVIDA      :",dvd,", ",dvd+(dvd*0.1),", ",dvd+(dvd*0.15),", ",dvd+(dvd*0.2),", ",dvd+(dvd*0.25))
print("VALOR DOS JUROS      :",dvd*0,"  , ",dvd*0.1," , ",dvd*0.15," , ",dvd*0.2," , ",dvd*0.25)
print("QUANTIDADE DE PARCELA:   1   ,   3    ,   6    ,   9   ,   12   ")
print("VALOR DA PARCELA     :",dvd,", ",int((dvd+(dvd*0.1))/3),", ",int((dvd+(dvd*0.15))/6),", ",int((dvd+(dvd*0.2))/9),", ",int((dvd+(dvd*0.15))/12))