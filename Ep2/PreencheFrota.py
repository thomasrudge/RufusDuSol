def preenche_frota (frota , nome , linha2 , coluna2 , orientacao2, tamanho2 ):
    
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
    

    listadeposicoes = []
    listadeposicoes.append(define_posicoes(linha2,coluna2,orientacao2,tamanho2))
    
    if nome not in frota:

        frota[nome] = listadeposicoes

    else:
        frota[nome].append(define_posicoes(linha2,coluna2,orientacao2,tamanho2))

    return frota