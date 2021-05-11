def ganhou_ou_perdeu(baralho):
    if len(baralho) > 1:
        a='perdeu'
        print("Você \033[031m{}".format(a))
        print(" ")
    else:
        b='Ganhou'
        print("Você \033[32m{}".format(b))
        print(" ")
