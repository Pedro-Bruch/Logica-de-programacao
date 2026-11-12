//Peça ao usuário três números e verifique se eles podem formar um triângulo. 
//Se sim, verifique se é "Equilátero", "Isósceles" ou "Escaleno".

programa {
  funcao inicio() {
    
    real lado1, lado2, lado3

    escreva("Digite o primeiro número: ")
    leia(lado1)
    escreva("Digite o segundo número: ")
    leia(lado2)
    escreva("Digite o terceiro número: ")
    leia(lado3)

    se (lado1 <= 0 ou lado2 <= 0 ou lado3 <= 0){
    escreva("Não pode ser um triângulo.")
    }senao{
    se (lado1 == lado2 e lado2 == lado3){
      escreva("É um triângulo Equilátero.")
    } senao{
      se (lado1 == lado2 ou lado2 == lado3 ou lado3 == lado1){
        escreva("É um triângulo Isosceles.")
      } senao{
        escreva("É um triângulo Escaleno")
      }
      }
    }
  }
}