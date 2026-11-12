//Peça para o usuário inserir três números e imprima o maior e o menor entre eles.

programa {
  funcao inicio() {
    
    inteiro numero1, numero2, numero3, maior, menor

    escreva("Escreva o 1 número: ")
    leia(numero1)
    escreva("Escreva o 2 número: ")
    leia(numero2)
    escreva("Escreva o 3 número: ")
    leia(numero3)

    maior = numero1
    menor = numero1

    se (numero2 > maior){
      maior = numero2
      se (numero3 > maior){
        maior = numero3
      }
    } senao{
      menor = numero2
      se (numero3 > numero2){
        menor = numero2
      } senao{
        menor = numero3
      }
    }
    escreva(maior," e " , menor)
  }
}
