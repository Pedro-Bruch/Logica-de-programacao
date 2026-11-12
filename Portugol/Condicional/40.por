//40.	Peça ao usuário para inserir um número inteiro. O programa deve verificar se o número é par ou ímpar e positivo ou negativo,
//e então exibir uma mensagem com essas classificações. Se o número for igual a zero, o programa deve indicar que é zero, 
//que não é nem positivo nem negativo, nem par nem ímpar.

programa {
  funcao inicio() {
     
     inteiro numero
     
     escreva("Digite um número: ")
     leia(numero)
     
     se (numero == 0){
      escreva("Seu número é zero.\nEle não é nem par/ímpar ou positivo/negativo.")
     } senao{

     se (numero % 2 == 0){
      se(numero < 0){
        escreva("Seu número é par e negativo. ")
      } senao{
        escreva("Seu número é par e positivo. ")
      }
     } senao{
      se(numero < 0){
        escreva("Seu número é ímpar e negativo.")
      } senao{
        escreva("Seu número é ímpar e positivo.")
      }
      }
     }
  }
}
