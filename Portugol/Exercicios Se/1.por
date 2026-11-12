//Leia um número. Informe se ele é positivo ou negativo.
programa {
  funcao inicio() {
    real numero
    escreva("Escreva um numero: ")
    leia(numero)
    se (numero == 0) {
      escreva("Seu número é neutro")
    } senao {
      se(numero > 0) {
      escreva("Seu número é positivo.")
      }senao {
        escreva("Seu numero é negativo")
      }
    }
  }
}
