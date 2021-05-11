import extrair_naipe
import extrair_valor

def lista_movimentos_possiveis (cartas,indice):
    valor= extrair_valor.extrai_valor(cartas[indice])
    naipe= extrair_naipe.extrai_naipe(cartas[indice])
    valorant= extrair_valor.extrai_valor(cartas[indice-1])
    naipeant= extrair_naipe.extrai_naipe(cartas[indice-1])
    valorterc= extrair_valor.extrai_valor(cartas[indice-3])
    naipeterc= extrair_naipe.extrai_naipe(cartas[indice-3])
    movimento=[]
    if indice == 0:
        return movimento
    elif indice < 3:
        if valor == valorant or naipe == naipeant:
            movimento.append(1)
            return movimento
    else:
        if (valor == valorant or naipe == naipeant) and (valor == valorterc or naipe == naipeterc):
            movimento.append(1)
            movimento.append(3)
            return movimento
        elif valor == valorant or naipe == naipeant:
            movimento.append(1)
        elif valor == valorterc or naipe == naipeterc:
            movimento.append(3)
            return movimento
    return movimento

