import Lista_movimentos

def possui_movimentos_possiveis(baralho,indice):
    c = indice
    while c < len(baralho):
        movimento = Lista_movimentos.lista_movimentos_possiveis(baralho, c)
        if movimento != []:
            return True
        c += 1
    return False
  