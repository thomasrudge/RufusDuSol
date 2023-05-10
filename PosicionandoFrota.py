def afundados(frotas, tabuleiro):
    afundados = 0
    for ship in frotas:
        for posicao in frotas[ship]:
            afundado = True
            for coord in posicao:
                if tabuleiro[coord[0]][coord[1]] != "X":
                    afundado = False
                    break
            if afundado:
                afundados += 1
    return afundados


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

def faz_jogada(tabuleiro , linha , coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"

    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro


def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    cond = False
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

    posicoes = define_posicoes (linha, coluna, orientacao, tamanho)

    if orientacao == 'vertical' and linha + tamanho > 10:
        return cond
    if orientacao == 'horizontal' and coluna + tamanho > 10:
        return cond
    

    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        for tipo, posicoes in frota.items():
            for posicao in posicoes:
                for linha_frota, coluna_frota in posicao:
                    if linha == linha_frota and coluna == coluna_frota:
                        return cond

    cond = True    
    return cond


def posiciona_frota(frota):

    listas = []

    tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    

    for i in frota.values():
        for coord in i:
            listas.append(coord)

    

    for i in listas:
        for coord2 in i:
            tabuleiro[coord2[0]][coord2[1]] = 1

    

    

    return tabuleiro


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


nomes = ["porta-aviões" , "navio-tanque" , "navio-tanque" , "contratorpedeiro" ,"contratorpedeiro" , "contratorpedeiro" , "submarino","submarino","submarino","submarino"]

tamanhos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

frota = {}

for i in range(10):

    condic = False

    while condic == False:
        print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(nomes[i] , tamanhos[i]))
        linha2 = int(input("Linha: "))
        coluna2 = int(input("Coluna: "))

        if nomes[i] == "submarino":
            orientacao2 = 1
            tamanho2 = 1
        else:
            orientacao2 = int(input("[1] Vertical [2] Horizontal >"))
            tamanho2 = tamanhos[i]




        



    
        orientacao = ""

        if orientacao2 == 1:
            orientacao = "vertical"
        elif orientacao2 == 2:
            orientacao = "horizontal"

        CouE = posicao_valida(frota , linha2 , coluna2 , orientacao , tamanho2)

        if CouE == False:
            print("Esta posição não está válida!")
        else:
            condic = True

    
    preenche_frota(frota , nomes[i] , linha2 , coluna2 , orientacao , tamanhos[i])
    

print(frota)