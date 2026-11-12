//Solicite um número e verifique se ele é múltiplo de 7 e 3. Exiba "Sim" ou "Não".

programa {
  funcao inicio() {
    
    inteiro numero

    escreva("Digite um número: ")
    leia(numero)

    se (numero % 3 == 0 ou numero % 7 == 0){
      escreva("sim")
    } senao{
      escreva("não")
    }
  }
}
