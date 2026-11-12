//6.	Crie um programa que ajude a programar turnos de trabalho em uma empresa. 
//O usuário deve informar o dia da semana (1 a 7, sendo 1 para domingo e 7 para sábado). O programa deve exibir a programação dos turnos:
//Dias úteis (segunda a sexta): Turno Normal
//Sábado: Turno Reduzido
//Domingo: Sem Trabalho
programa {
  funcao inicio() {
    
    inteiro diaDaSemana

    escreva("Qual o dia da semana?: \n1- Domingo\n2- Segunda\n3- Terça\n4- Quarta\n5- Quinta\n6- Sexta\n7- Sábado\n")
    leia(diaDaSemana)

    se (diaDaSemana == 1){
      escreva("Sem trabalho.")
    } senao{
      se (diaDaSemana >= 2 e diaDaSemana <= 6){
        escreva("Turno Normal.")
      } senao{
        escreva("Turno reduzido.")
      }
    }
  }
}
