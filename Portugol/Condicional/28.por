//28.	Escolher entre dois tipos de desconto
//Solicite o valor de uma compra e, dependendo do valor, ofereça um dos dois tipos de desconto:
//a.	Menor que 100: "Desconto de 5%"
//b.	Maior ou igual a 100: "Desconto de 10%"


programa {
  funcao inicio() {
    
    real valor, conta, valorDesconto

    escreva("Digite o valor da compra: ")
    leia(valor)

    se (valor < 100){
      valorDesconto = valor * 0.05
      conta = valor - valorDesconto
      escreva("O desconto de 5% é: ", valorDesconto ,"\nO valor a pagar com desconto é: ", conta)
    } senao{
      valorDesconto = valor * 0.1
      conta = valor - valorDesconto
      escreva("O desconto de 10% é: ", valorDesconto ,"\nO valor a pagar com desconto é: ", conta)
    }
  }
}
