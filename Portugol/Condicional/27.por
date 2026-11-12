//Você deve criar um programa que classifique a nota de um aluno em uma das categorias. O usuário deve inserir a nota do aluno (de 0 a 10), e o programa deve exibir a categoria da nota.
//As categorias de classificação são:
//●	A: Para notas entre 9.0 e 10.0.
//●	B: Para notas entre 7.0 e 8.9.
//●	C: Para notas entre 5.0 e 6.9.
//●	D: Para notas entre 3.0 e 4.9.
//●	E: Para notas entre 0.0 e 2.9.


programa {
  funcao inicio() {

    real nota

    escreva("Digite sua nota: ")
    leia(nota)

    se ( nota < 3){
      escreva("Sua classificação é E")
    } senao{
      se (nota >= 3 e nota < 5){
        escreva("Sua classificação é D")
      } senao{
        se (nota >= 5 e nota < 7){
          escreva("Sua classificação é C")
        } senao{
          se (nota >= 7 e nota < 9){
            escreva("Sua classificação é B")
          } senao{
            escreva("Sua classificação é A")
          }
        }
      }
    }
  }
}
