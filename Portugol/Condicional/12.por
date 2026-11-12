//Solicite dois números ao usuário e imprima o maior deles.
programa {
  funcao inicio() {
    
    real numero1, numero2

    escreva("Digite um número: ")
    leia(numero1)
    escreva("Digite outro número: ")
    leia(numero2)

    se (numero1 > numero2){
      escreva("O número ", numero1 , " é maior que o ", numero2)
    } senao{
      escreva("O número ", numero2 , " é maior que o ", numero1)
    }
  }
}
