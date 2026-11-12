//39.	Determinar o vencedor de uma eleição
//Solicite ao usuário o número de votos para três candidatos e determine qual candidato obteve a maior quantidade de votos, considerando que pode haver empate.


programa {
  funcao inicio() {
    
    inteiro cand1, cand2, cand3

    escreva("Digite votos do candidato 1: ")
    leia(cand1)
    escreva("Digite votos do candidato 2: ")
    leia(cand2)
    escreva("Digite votos do candidato 3: ")
    leia(cand3)

    escreva("Candidato 1 teve: ", cand1, " votos.\nCandidato 2 teve: ", cand2 ," votos.\nCandidato 3 teve: ", cand3," votos.")
    se (cand1 == cand2 e cand2 == cand3){
      escreva("\nEmpate dos 3 candidatos")
    } senao{
    se (cand1 == cand2 e cand1 > cand3){
      escreva("\nEmpate na liderança entre candidato 1 e 2. ",cand1," votos." )
    } senao se (cand2 == cand3 e cand2 > cand3){
      escreva("\nEmpate na liderança entre candidato 2 e 3.",cand2," votos.")
    } senao se(cand1 == cand3 e cand1 > cand2){
      escreva("\nEmpate na liderança entre candidato 1 e 3.",cand3," votos.")
    } senao {
      se (cand1 > cand2 e cand1 > cand3){
        escreva("\nO candidato 1 ganhou com ", cand1," votos.")
      } senao se(cand2 > cand3){
        escreva("\nO candidato 2 ganhou com ", cand2," votos.")
      } senao {
        escreva("\nO candidato 3 ganhou com ", cand3," votos.")
      }
      }
    }
  }
}
