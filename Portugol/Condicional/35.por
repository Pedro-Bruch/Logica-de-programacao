//35.	Conversor de unidades de temperatura
//Solicite ao usuário um valor em Celsius e permita que ele escolha converter para Fahrenheit ou Kelvin.

programa {
  funcao inicio() {
    
    real tempCelsius, temp, conta

    escreva("Digite a temperatura em Celsius: ")
    leia(tempCelsius)
    escreva("Digite para qual escala deseja converter:\n1- Fahrenheit\n2- Kelvin\n")
    leia(temp)

    se( temp == 1){
      conta = (tempCelsius * 1.8) + 32
      escreva("Sua temperatura em Fahrenheit é: ", conta)
    } senao{
      conta = tempCelsius + 273.15
      escreva("Sua temperatura em Kelvin é: ", conta)
    }
  }
}
