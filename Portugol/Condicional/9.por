//9.	Crie um programa que calcule o desconto a ser aplicado em uma compra. 
//O usuário deve informar o valor total da compra e o tipo de cliente (Regular, VIP ou Funcionário). As regras para o desconto são:
//Regular: 0% de desconto
//VIP: 10% de desconto
//Funcionário: 20% de desconto
programa {
  funcao inicio() {
    
    real valorCompra, tipoCliente, conta

    escreva("Digite o valor da compra: ")
    leia(valorCompra)
    escreva("Qual o tipo de cliente:\n1-Regular\n2-VIP\n3-Funcionário\n")
    leia(tipoCliente)

    se (tipoCliente == 2){
        conta = valorCompra - (valorCompra * 0.1)
        escreva("O valor com desconto é: ", conta)
    } senao{ 
      se (tipoCliente == 3){
        conta = valorCompra - (valorCompra * 0.2)
        escreva("O valor com desconto é: ", conta)
      } senao{
        escreva("Não há desconto, o valor é: ", valorCompra)
      }
    }
  }
}
