def lista_movimentos_possiveis (cartas,indice):
    lugar = cartas[indice]
    movimento=[]
    if indice == 0:
        return movimento
    elif lugar[0] == cartas[indice-1][0] or lugar[1] ==cartas[indice-1][1] :
        movimento.append(1)
    if lugar[0] == cartas[indice-3] or lugar[1] == cartas[indice-3][1]:
        movimento.append(3)

    return movimento

        



print(lista_movimentos_possiveis(['A♠', 'J♠', 'Q♠', 'K♠', '10♠'],1))