//Solicite ao usuário seu peso e altura e calcule o IMC. De acordo com o valor do IMC, classifique:
//a.	Menor que 18.5: "Abaixo do peso"
//b.	Entre 18.5 e 24.9: "Peso normal"
//c.	Entre 25 e 29.9: "Sobrepeso"
//d.	Maior que 30: "Obesidade"


programa {
  funcao inicio() {
    
    real peso, altura, imc

    escreva("Digite seu peso: ")
    leia(peso)
    escreva("Digite sua altura(em  metros): ")
    leia(altura)

    imc = peso / (altura * altura)

    se(imc < 18.5){
      escreva("Abaixo do peso")
    }senao{
      se (imc >= 18.5 e imc < 25){
        escreva("Peso normal")
      }senao{
        se (imc >= 25 e imc <30){
          escreva("Sobrepeso")
        }senao{
          escreva("Obesidade")
        }
      }
    }
  }
}
