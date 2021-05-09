import Lista_movimentos

def possui_movimentos_possiveis(baralho):
    c = 0
    s=0
    while c < len(baralho):
        movimentos = Lista_movimentos.lista_movimentos_possiveis(baralho, c)
        if len(movimentos) != 0:
            s +=1
        c += 1

    if s !=0:
        return True
    else:       
        return False
  
    