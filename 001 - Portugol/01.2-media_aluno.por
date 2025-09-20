programa {
  funcao inicio() {
    // Programa para calcular a média de um aluno com base em três notas

    // Criação das variáveis
    cadeia nome
    real nota1
    real nota2
    real nota3
    real media

    // Solicitação dos dados ao usuário
    escreva("Digite o nome do aluno: ")
    leia(nome)
    escreva("Digite a primeira nota: ")
    leia(nota1)
    escreva("Digite a segunda nota: ")
    leia(nota2)
    escreva("Digite a terceira nota: ")
    leia(nota3)

    // Realização do cálculo da média e armazenamento na variável media
    media = (nota1 + nota2 + nota3) / 3

    // Apresentando ao usuário a média do aluno
    escreva("A média do aluno ", nome, " é ", media)

  }
}
