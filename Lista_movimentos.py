def lista_movimentos_possiveis (cartas,indice):
    lugar = cartas[indice]
    movimento=[]
 #valor/numero
    if indice == 0:
        return movimento
    elif lugar[0] == cartas[indice-1][0] or lugar[1] ==cartas[indice-1][1] :
        movimento.append(1)
    elif len(cartas[indice-1]) == 3:
        if lugar[1] == cartas[indice-1][2]:
            movimento.append(1)
    elif len(lugar) == 3:
        if lugar[2] == cartas[indice-1][1]:
            movimento.append(1)
    
 #naipe
    if indice ==1 or indice ==2:
        return movimento
    elif lugar[0] == cartas[indice-3] or lugar[1] == cartas[indice-3][1]:
        movimento.append(3)
    elif len(cartas[indice-3]) == 3:
        if lugar[1] == cartas[indice-3][2]:
            movimento.append(3)
    elif len(lugar) == 3:
        if lugar[2] == cartas[indice-3][1]:
            movimento.append(3)
    return movimento
