#funcao que verifica se o movimento pode ou nao ser feito

import Lista_movimentos

def possui_movimentos_possiveis(baralho):
    c = 0
    s=0
    while c < len(baralho):
        movimento = Lista_movimentos.lista_movimentos_possiveis(baralho, c)
        if len(movimento) != 0:
            s +=1
        c += 1

    if s !=0:
        return True
    else:       
        return False
  