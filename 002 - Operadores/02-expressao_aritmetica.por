programa {
  funcao inicio() {
    // Programa para calcular a porcentagem de um valor
    
    // Criação das variáveis
    real valor_total
    real porcentagem
    real valor_parte
          
    // Solicitando dados ao usuário
    escreva("Digite o valor total: ")
    leia(valor_total)
    escreva("Digite a porcentagem (%): ")
    leia(porcentagem)

    // Realizando o cálculo de porcentagem
    valor_parte = valor_total * (porcentagem / 100)
        
    // Apresentando o resultado do cálculo de porcentagem
    escreva(porcentagem, "% de ", valor_total, " é: ", valor_parte)
    }
}

