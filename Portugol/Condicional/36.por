//36.	Ordenação de três números
//Solicite três números e ordene-os em ordem crescente utilizando apenas estruturas de condição.


programa {
  funcao inicio() {
    
    inteiro numero1, numero2, numero3, maior, menor, medio

    escreva("Escreva o 1 número: ")
    leia(numero1)
    escreva("Escreva o 2 número: ")
    leia(numero2)
    escreva("Escreva o 3 número: ")
    leia(numero3)

    maior = numero1
    menor = numero1
    medio = numero1

    se (numero2 > maior){
      maior = numero2
      medio = numero1
      menor = numero3
      se (numero3 > maior){
        maior = numero3
        medio = numero2
        menor = numero1
      }
    } senao{
      menor = numero3
      medio = numero2
      se (numero3 > maior){
        maior = numero3
        medio = numero1
        menor = numero2
      } senao{
        menor = numero3
        medio = numero2
      }
    }
    escreva(maior,",", medio,",", menor)
  }
}
