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