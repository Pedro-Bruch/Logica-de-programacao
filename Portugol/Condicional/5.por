//5.Crie um programa que simule uma calculadora simples. O usuário deve informar a operação desejada e os dois números para realizar o cálculo.
//As operações podem ser: adição, subtração, multiplicação e divisão.
programa {
  funcao inicio() {
    
    real numero, numero2, sinal, conta

    escreva("Escreva o primeiro número: ")
    leia(numero)
    escreva("Escreva o segundo número: ")
    leia(numero2)
    escreva("Qual sinal deseja utilizar?\n1 +\n2 -\n3 *\n4 /\n")
    leia(sinal)

    se (sinal == 1){
      conta = numero + numero2
      escreva("A soma dos números é: " , conta)
    } senao{
      se (sinal == 2){
        conta = numero - numero2
        escreva("A subtração dos números é: " , conta)
      } senao{
        se (sinal == 3){
          conta = numero * numero2
          escreva("A multiplicação dos números é: " , conta)
        } senao{
          conta = numero / numero2
          escreva("A divisão dos núemros é: ", conta)
        }
      }
    }
  }
}
