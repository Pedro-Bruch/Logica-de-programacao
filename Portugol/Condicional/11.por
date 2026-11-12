//11.	Verificar se um número é positivo ou negativo
//Peça ao usuário para inserir um número e imprima se o número é "Positivo" ou "Negativo".

programa {
  funcao inicio() {

    real numero

    escreva("Digite um número: ")
    leia(numero)    
    
    se (numero == 0){
      escreva("Seu número é neutro.")
    } senao{
      se (numero < 0){
        escreva("Seu número é negativo.")
      } senao{
        escreva("Seu número é positivo.")
      }
    }
    
  }
}