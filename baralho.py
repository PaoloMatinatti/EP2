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
        if c2 <=13-1:
            espadas= cartas[c2]+ '♠'
            baralho.append('\033[34m{}\033[m'.format(espadas))
            c2+=1
            i+=1
        if c3 <=13-1:
           copas= cartas[c3]+ '♥'
           baralho.append('\033[31m{}\033[m'.format(copas))
           c3+=1
           i+=1
        if c4 <=13-1:
            ouros= cartas[c4]+ '♦'
            baralho.append('\033[33m{}\033[m'.format(ouros))
            c4+=1
            i+=1
        else:
            caralos = False
    random.shuffle(baralho)
    return baralho





   




