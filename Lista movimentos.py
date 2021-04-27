def lista_movimentos_possiveis (cartas,indice):
    lugar = cartas[indice]
    movimento=[]
 #verifica numero e naipe pra 10  
    if lugar[0] + lugar [1] == '10' :
        if lugar[1] == cartas[indice-1][1] or lugar[2] == cartas[indice-1][1]:
                movimento.append(1)
        if lugar[1] == cartas[indice-3][1] or lugar[2] == cartas[indice-3][1] :
                movimento.append(3)
        return movimento
 #verifica o numero
    if indice == 0:
        return movimento
    elif lugar[0] == cartas[indice-1][0] or lugar[1] ==cartas[indice-1][1] or lugar[1] == cartas[indice-1][2] :
        movimento.append(1)
 #verifca o naipe
    if indice ==1 or indice ==2:
        return movimento
    elif lugar[0] == cartas[indice-3][0] or lugar[1] == cartas[indice-3][1] or lugar[1] == cartas[indice-3][2]:
        movimento.append(3)

    

    return movimento  
print(lista_movimentos_possiveis(['10♦', '10♥', '10♣', '10♠', '10♣'],4))