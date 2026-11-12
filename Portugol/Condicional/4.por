// 4.	A concessionária de veículos “CARANGO” está vendendo os seus veículos com desconto. 
//Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente.
//O desconto deverá ser calculado sobre o valor do veículo de acordo com o combustível (álcool – 25%, gasolina – 21% ou diesel –14%). 
programa {
  funcao inicio() {

    real valor, valorDesconto, valorPago, combustivel

    escreva("Digite o valor do veículo: ")
    leia(valor)
    escreva("Qual tipo de combustível deseja utilizar?\n1- Álcool\n2- Gasolina\n3- Diesel\n")
    leia(combustivel)

    se (combustivel == 1){
      valorDesconto = valor * 0.25
      valorPago = valor - valorDesconto 
      escreva("O valor de desconto é: R$ " , valorDesconto , "\nO valor a ser pago é: R$ " , valorPago)
    } senao se (combustivel == 2){
      valorDesconto = valor * 0.21
      valorPago = valor - valorDesconto 
      escreva("O valor de desconto é: R$ " , valorDesconto , "\nO valor a ser pago é: R$ " , valorPago)
    } senao {
      valorDesconto = valor * 0.14
      valorPago = valor - valorDesconto 
      escreva("O valor de desconto é: R$ " , valorDesconto , "\nO valor a ser pago é: R$ " , valorPago)
    }
  }
}
