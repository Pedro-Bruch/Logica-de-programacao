//Peça para o usuário escolher uma operação (soma, subtração, multiplicação, divisão) e dois números. Realize a operação e mostre o resultado.

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
