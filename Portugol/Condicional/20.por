//Solicite ao usuário um número de 1 a 7 e imprima o nome do dia correspondente. Exemplo: 1 = "Domingo", 2 = "Segunda-feira", etc.

programa {
  funcao inicio() {
    
    inteiro dia

    escreva("Digite um número da semana: ")
    leia(dia)

    se (dia == 1){
      escreva("É domingo.")
    } senao{
      se (dia == 2){
      escreva("É segunda.")
    } senao {
      se (dia == 3){
      escreva("É terça.")
    } senao{
      se (dia == 4){
      escreva("É quarta.")
    } senao {
      se (dia == 5){
      escreva("É quinta.")
    } senao {
      se (dia == 6){
      escreva("É sexta.")
    } senao{
      se (dia ==7)
      escreva("É sábado.")
    }
    }
    }
    }
    }
    }
  }
}
