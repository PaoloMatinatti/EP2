#funcao que recebe um carta e extrai o naipe dela.
def extrai_naipe(carta):
    if carta[5]=='1':
        return(carta[7])
    else:
        return(carta[6]) 

