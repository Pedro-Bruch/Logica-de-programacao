//Leia uma distância em quilômetros e transforme em metros.
programa {
  funcao inicio() {
    real quilometro, metro
    escreva("Escreva sua distancia em quilômetros: ")
    leia(quilometro)
    metro = quilometro * 1000
    escreva("Sua distância em metros é: " , metro)    
  }
}
