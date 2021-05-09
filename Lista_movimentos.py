import extrair_naipe
import extrair_valor

def lista_movimentos_possiveis(baralho,ind):


    naipe_carta = extrair_naipe.extrai_naipe(baralho[ind])

    naipe_anterior = extrair_naipe.extrai_naipe(baralho[ind-1])

    valor_carta = extrair_valor.extrai_valor(baralho[ind])

    valor_anterior = extrair_valor.extrai_valor(baralho[ind-1])

    if ind == 0:  

        return []

    elif ind < 3:

        if naipe_carta == naipe_anterior or valor_carta == valor_anterior:

            return [1]

        else:

            return []

    elif ind >= 3:

        naipe_terceiro = extrair_naipe.extrai_naipe(baralho[ind-3])

        valor_terceiro = extrair_valor.extrai_valor(baralho[ind-3])

        if valor_carta == valor_anterior and valor_carta == valor_terceiro:

            return [1, 3]

        elif naipe_carta == naipe_anterior and naipe_carta == naipe_terceiro:

            return [1, 3]

        elif valor_carta == valor_anterior and naipe_carta == naipe_terceiro:

            return [1, 3]

        elif naipe_carta == naipe_anterior and valor_carta == valor_terceiro:

            return [1, 3]

        elif naipe_carta == naipe_anterior or valor_carta == valor_anterior:

            return [1]

        elif valor_carta == valor_terceiro or naipe_carta == naipe_terceiro:

            return [3]

        else:

            return []

    else:

        return []
