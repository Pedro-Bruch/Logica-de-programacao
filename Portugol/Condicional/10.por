//Desenvolva um programa que avalie o desempenho de um funcionário com base em sua pontuação. O usuário deve informar a pontuação do funcionário. O programa deve classificar o desempenho da seguinte maneira:
//●	0 a 5: Insatisfatório
//●	6 a 8: Satisfatório
//●	9 a 10: Excelente


programa {
  funcao inicio() {
    
    inteiro pontuacao

    escreva("Digite a pontuação do cliente: ")
    leia(pontuacao)

    se (pontuacao <= 0 e pontuacao <= 5){
      escreva("Insatisfatório.")
    } senao{
      se (pontuacao >= 6 e pontuacao <= 8){
        escreva("Satisfatório.")
      } senao {
        escreva("Excelente.")
      }
    }
  }
}
