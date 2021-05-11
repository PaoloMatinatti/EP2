import random
def cria_baralho ():
    baralho= []
    cartas= ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    c=0
    c2=0
    c3=0
    c4=0
    i=0
    caralos = True
    while caralos:
        if c <= 13 -1:
            paus= cartas[c] + '♣'
            baralho.append('\033[35m{}\033[m'.format(paus))
            c+=1
            i+=1

        else:
            caralos = False
    random.shuffle(baralho)
    return baralho





   




