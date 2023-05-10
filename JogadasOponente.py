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




frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

#print(frota)
#print(frota_oponente)

lista_linha_coluna_ataque_oponente_anterior = []

jogando = True


posicoes_atacadas = []

tabuleiro_oponente = posiciona_frota(frota_oponente)

while jogando == True:

    


    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '___________      ___________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto

    




   

    tabuleiro_jogador = posiciona_frota(frota)
    

    
    
    
    
    

   

   
    
    jogadaLinha = int(input("Qual linha voce deseja atacar? "))
    jogadaColuna = int(input("Qual coluna voce deseja atacar? "))

    validos = [0,1,2,3,4,5,6,7,8,9]

    if jogadaLinha not in validos:
        print("Linha inválida!")

    elif jogadaColuna not in validos:
        print("Coluna inválida!")

    

    else:

    

        if [jogadaLinha , jogadaColuna] in posicoes_atacadas:
            print('A posição linha LINHA e coluna COLUNA já foi informada anteriormente!')
        else:
            posicoes_atacadas.append([jogadaLinha , jogadaColuna])
            faz_jogada(tabuleiro_oponente , jogadaLinha , jogadaColuna)
            print(monta_tabuleiros(tabuleiro_jogador , tabuleiro_oponente))
   

        if afundados(frota_oponente , tabuleiro_oponente) == 10:
            print("'Parabéns! Você derrubou todos os navios do seu oponente!'")
            jogando = False

# jogadas do oponente
    import random
    # jogadas do oponente
    linha_coluna_oponente_invalida = True
    while linha_coluna_oponente_invalida:
        linha_ataque_oponente = random.randint(0,9)
        coluna_ataque_oponente = random.randint(0,9)
        
        lista_linha_coluna_ataque_oponente =[linha_ataque_oponente, coluna_ataque_oponente]
        
        if lista_linha_coluna_ataque_oponente not in lista_linha_coluna_ataque_oponente_anterior:
            lista_linha_coluna_ataque_oponente_anterior.append(lista_linha_coluna_ataque_oponente)
            linha_coluna_oponente_invalida = False
            print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_ataque_oponente, coluna_ataque_oponente))
            novo_tabuleiro = faz_jogada(tabuleiro_jogador, linha_ataque_oponente, coluna_ataque_oponente)
            quantos_afundados = afundados (frota, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False