programa {
    funcao inicio() {
      // Programa para demonstrar o uso de operadores lógicos
      
      // Criação das variáveis
      inteiro a
      inteiro b
      inteiro c

      // Solicitação dos valores de a, b e c ao usuário
      escreva("Digite o valor para variável A: ")
      leia(a)
      escreva("Digite o valor para variável B: ")
      leia(b)
      escreva("Digite o valor para variável C: ")
      leia(c)

      // Apresentação do resultado dos operadores lógicos ao usuário
      escreva("Comparações:\n")
      escreva("(a > b) E (c == b) = ", (a > b e c == b), "\n")
      escreva("(a < b) OU (c > b) = ", (a < b ou c > b), "\n")
      escreva("NAO (a != b) = ", nao (a != b), "\n")
    }
}
