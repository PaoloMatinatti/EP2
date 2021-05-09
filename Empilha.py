 #funcao q recebe um baralho posicao inicial(pi) e uma posicao de destino (pf)
def empilha (baralho,pi,pf):
    
    variavel =True
    while variavel:
        baralho[pf] = baralho[pi]
        del baralho[pi]
        break
        

    return baralho

