// Leia uma temperatura em Celsius e converta para Fahrenheit.  Fórmula: F = (C × 9/5) + 32
programa {
  funcao inicio() {
    real celsius, conta
    escreva("Escreva temperatura em Celsius: ")
    leia(celsius)
    conta = (celsius * 9/5) + 3
    escreva("O valor em Fahrenheit é: " , conta)    
  }
}
