//Peça para o usuário inserir um número e mostre se ele é "Par" ou "Ímpar".
programa {
  funcao inicio() {
    
    inteiro numero

    escreva("Digite seu número: ")
    leia(numero)

    se (numero % 2 == 0){
      escreva("Seu número é par.")
    } senao{
      escreva("Seu número é ímpar.")
    }
  }
}
