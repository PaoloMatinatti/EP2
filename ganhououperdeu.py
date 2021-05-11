def ganhou_ou_perdeu(baralho):
    if baralho > 1:
        a='perdeu'
        print("Você \033[031m{}\033[m".format(a))
        print(" ")
        jogar_de_novo = str(input("Quer de jogar de novo? (digite S ou N): "))
        return jogar_de_novo
    else:
        b='Ganhou'
        print("Você \033[32m{}\033[m".format(b))
        print(" ")
        jogar_de_novo = str(input("Quer de jogar de novo? (digite S ou N): "))
        return jogar_de_novo