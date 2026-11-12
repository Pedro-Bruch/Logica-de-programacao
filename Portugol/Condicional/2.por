//Faça um programa que leia o seu peso na Terra e o número de um planeta e calcule qual será o seu peso neste planeta.
//A relação de planetas é:   Nº PlanetaGravidade Relativa 
//1 Mercúrio 0,37 2 Vênus 0,88 3 Marte 0,38 4 Júpiter 2,64 5 Saturno1,15 6 Urano1,17
//A fórmula para o cálculo do peso em outro planeta, considerando a gravidade relativa de cada um deles é:   
//PesoNoPlaneta = (pesoNaTerra / 10) * gravidade

programa {
  funcao inicio() {

    real peso, numeroPlaneta, pesoNovo

    escreva("Escreva seu peso: ")
    leia(peso)
    escreva("Qual planeta deseja escolher?\n1- Mercúrio\n2- Vênus\n3- Marte\n4- Júpiter\n5- Saturno\n6- Urano\n")
    leia(numeroPlaneta)

    se (numeroPlaneta == 1){
      pesoNovo = (peso / 10) * 0.37
      escreva("Seu peso no planeta Mercúrio é: ", pesoNovo , "kg")
    } senao{
      se (numeroPlaneta == 2){
        pesoNovo = (peso / 10) * 0.88
        escreva("Seu peso no planeta Vênus é: ", pesoNovo , "kg")
      } senao{
        se (numeroPlaneta == 3){
        pesoNovo = (peso / 10) * 0.38
        escreva("Seu peso no planeta Marte é: ", pesoNovo , "kg")
      } senao{
        se (numeroPlaneta == 4){
        pesoNovo = (peso / 10) * 2.64
        escreva("Seu peso no planeta Júpiter é: ", pesoNovo , "kg")
      } senao{
        se (numeroPlaneta == 5){
        pesoNovo = (peso / 10) * 1.15
        escreva("Seu peso no planeta Saturno é: ", pesoNovo , "kg")
      } senao{
        pesoNovo = (peso / 10) * 1.17
        escreva("Seu peso no planeta Urano é: ", pesoNovo , "kg")
      }
      }
      }
      }
      }
    }
  }
}
