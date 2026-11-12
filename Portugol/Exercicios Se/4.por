// Leia dois números. Informe qual deles é maior. Considere também a possibilidade de serem iguais.
programa {
  funcao inicio() {
    real numero1, numero2
    escreva("Digite um número: ")
    leia(numero1)
    escreva("Digite outro número:")
    leia(numero2)
    se(numero1 == numero2){
      escreva("os numeros são iguais")
      }senao{
    se(numero1 > numero2){
      escreva("O " , numero1 , " é maior que o " , numero2)
    } senao{
      escreva("O " , numero2 , " é maior que o " , numero1)
    }}
  }
}
