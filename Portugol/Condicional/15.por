//Solicite um número e imprima "Sim" se ele for divisível por 3 ou por 5, e "Não" caso contrário.
programa {
  funcao inicio() {
    
    inteiro numero

    escreva("Digite um número: ")
    leia(numero)

    se (numero % 3 == 0 ou numero % 5 == 0){
      escreva("sim")
    } senao {
      escreva("Não")}
  } 
}
