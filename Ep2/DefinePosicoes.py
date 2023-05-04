def define_posicoes (linha , coluna , orientacao , tamanho):

    posicao = []

    posicao.append([linha,coluna])

    i = 0
    if orientacao == "vertical":
        while i < tamanho-1:
            linha += 1
            i += 1
            posicao.append([linha,coluna])

    elif orientacao == "horizontal":
        while i < tamanho-1:
            coluna += 1
            i+= 1
            posicao.append([linha,coluna])

    return posicao
    