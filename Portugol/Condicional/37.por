//37.	Simulação de um caixa eletrônico
//Solicite ao usuário o valor de um saque e verifique quantas notas de 100, 50, 20, 10 e 5 ele receberá.


programa {
  funcao inicio() {
    
    inteiro valor, n100, n50, n20, n10, n5, resto

    escreva("Quanto você deseja sacar?: ")
    leia(valor)
    
    se (valor % 5 != 0){
      escreva("Digite um número múltiplo de 5 para ser realizado o saque.")
    } senao{
      n100 = valor / 100
      resto = valor % 100

      n50 = resto / 50
      resto = valor % 50

      n20 = resto / 20
      resto = valor % 20

      n10 = resto / 10
      resto = valor % 10

      n5 = resto / 5
      resto = valor % 5

      escreva("As notas entregues serão:\nNotas de R$ 100: ", n100 ,"\nNotas de R$ 50: ", n50 , "\nNotas de R$ 20: ", n20 , "\nNotas de R$ 10: " , n10 ,"\nNotas de R$ 5: ", n5)
    }
  }
}
