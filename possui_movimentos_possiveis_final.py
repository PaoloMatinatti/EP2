import Lista_movimentos

<<<<<<< HEAD
def possui_movimentos_possiveis(baralho):
    c = 0
    s=0
=======
def possui_movimentos_possiveis(baralho,indice):
    c = indice 
>>>>>>> 19fcce7a956b2fff54a72a0706d6df0799cdd19e
    while c < len(baralho):
        movimento = Lista_movimentos(baralho, c)
        if len(movimento) != 0:
            s +=1
        c += 1

    if s !=0:
        return True
    else:       
        return False
  
    