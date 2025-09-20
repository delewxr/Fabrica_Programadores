programa {
  funcao inicio() {
    // Programa para calcular o preço final de um produto após aplicar um desconto

    // Declaração de variáveis
    real preco_original
    real porcentagem_desconto
    real valor_desconto
    real preco_final

    // Solicita o preço original
    escreva("Digite o preço original do produto: ")
    leia(preco_original)

    // Solicita a porcentagem de desconto
    escreva("Digite a porcentagem de desconto: ")
    leia(porcentagem_desconto)

    // Calcula o valor do desconto
    valor_desconto = preco_original * (porcentagem_desconto / 100)

    // Calcula o preço final com desconto
    preco_final = preco_original - valor_desconto

    // Exibe os resultados
    escreva("Valor do desconto: ", valor_desconto,"\n")
    escreva("Preço final do produto: ", preco_final)
    }
}


