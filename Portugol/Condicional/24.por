//Solicite um número e verifique se ele é primo (divisível apenas por 1 e por ele mesmo).

programa {
  funcao inicio() {
    
    inteiro numero

    escreva("Digite um número: ")
    leia(numero)

    se (numero == 2){
      escreva("Seu número é primo")
    } senao{
      se (numero == 1){
        escreva("Seu número é neutro")
      } senao{
        se (numero % 2 == 0 ou numero % 3 == 0 ou numero % 5 == 0 ou numero % 7 == 0){
        escreva("Seu número não é primo")
        } senao{
          escreva("Seu número é primo.")
        }
      }
    }
  }
}
