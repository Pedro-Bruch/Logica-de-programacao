// Leia um número inteiro e mostre seu antecessor e seu sucessor.
programa {
  funcao inicio() {
    inteiro numero, antecessor, sucessor
    escreva("Digite um numero: ")
    leia(numero)
    antecessor = numero - 1
    sucessor = numero + 1
    escreva("O antecessor do seu numero é " , antecessor , ", e o sucessor é " , sucessor)
  }
}
