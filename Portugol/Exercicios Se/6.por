//Crie um programa que ajude a programar turnos de trabalho em uma empresa. O usuário deve informar o dia da semana 
//(1 a 7, sendo 1 para domingo e 7 para sábado). O programa deve exibir a programação dos turnos:
//Dias úteis (segunda a sexta): Turno Normal
//Sábado: Turno Reduzido
//Domingo: Sem Trabalho
programa {
  funcao inicio() {
    inteiro diaDaSemana

    escreva("Digite o dia da semana: ")
    leia(diaDaSemana)

    se (diaDaSemana == 1){
      escreva("O dia da semana é Domingo. Sem trabalho.")
    } senao se(diaDaSemana == 2){
      escreva("O dia da semana é Segunda. Turno normal.")
    } senao se(diaDaSemana == 3){
      escreva("O dia da semana é Terça. Turno normal.")
    } senao se(diaDaSemana == 4){
      escreva("O dia da semana é Quarta. Turno normal.")
    } senao se(diaDaSemana == 5){
      escreva("O dia da semana é Quinta. Turno normal.")
    } senao se(diaDaSemana == 6){
      escreva("O dia da semana é Sexta. Turno normal.")
    } senao se(diaDaSemana == 7){
      escreva("O dia da semana é Sábado. Turno reduzido.")
    }
    }
  }
}
