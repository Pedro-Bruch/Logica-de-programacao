// Leia um número e mostre o dobro e o triplo.
programa {
  funcao inicio() {
    real numero, conta1, conta2
    escreva("Escreva um número: ")
    leia(numero)
    conta1 = numero * 3  
    conta2 = numero * 2
    escreva("O triplo do seu número é: " , conta1 , ", e o dobro é: " , conta2)  
  }
}
