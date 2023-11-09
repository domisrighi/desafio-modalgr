def calcular_notas_maior_valor(valor):
    notas_100 = valor // 100
    notas_50 = (valor % 100) // 50
    return notas_100, notas_50

def calcular_notas_menor_valor(valor):
    notas = [20, 10, 5, 2]
    notas_quantidade = []
    for nota in notas:
        quantidade = valor // nota
        notas_quantidade.append((quantidade, nota))
        valor %= nota
    return notas_quantidade

def escolher_opcao_retirada(valor):
    print("1. Notas de maior valor")
    print("2. Notas de menor valor")
    print("3. Notas mescladas")

    opcao = int(input("Opção escolhida: "))
    
    if opcao == 1:
        notas_100, notas_50 = calcular_notas_maior_valor(valor)
        print(f"{notas_100} x 100 reais")
        print(f"{notas_50} x 50 reais")
        valor_restante = valor - (notas_100 * 100) - (notas_50 * 50)
        if valor_restante > 0:
            notas_menor = calcular_notas_menor_valor(valor_restante)
            for quantidade, nota in notas_menor:
                if quantidade > 0:
                    print(f"{quantidade} x {nota} reais")
    elif opcao == 2:
        notas_menor = calcular_notas_menor_valor(valor)
        for quantidade, nota in notas_menor:
            if quantidade > 0:
                print(f"{quantidade} x {nota} reais")
    elif opcao == 3:
        metade_valor = valor // 2
        notas_100_metade, notas_50_metade = calcular_notas_maior_valor(metade_valor)
        notas_menor_metade = calcular_notas_menor_valor(valor - metade_valor)
        print(f"{notas_100_metade} x 100 reais")
        print(f"{notas_50_metade} x 50 reais")
        for quantidade, nota in notas_menor_metade:
            if quantidade > 0:
                print(f"{quantidade} x {nota} reais")
    else:
        print("Opção inválida. Escolha entre 1, 2 ou 3.")
        programa_emprestimo()

def programa_emprestimo():
    nome = input("Digite seu nome: ")
    anos_de_casa = float(input("Digite seus anos de casa: ".replace(",", ".")))
    salario = float(input("Digite seu salário atual: ".replace(",", ".")))
    valor_emprestimo = int(input("Digite o valor do empréstimo desejado: ".replace(",", ".")))

    if anos_de_casa <= 5 or valor_emprestimo > 2 * salario:
        print("Agradecemos seu interesse, mas você não atende aos requisitos mínimos do programa.")
    else:
        print(f"Olá, {nome}! Você solicitou um empréstimo de {valor_emprestimo} reais. Escolha uma opção de retirada:")
        escolher_opcao_retirada(valor_emprestimo)

programa_emprestimo()