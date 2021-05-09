def jogo_3(baralho):
    if baralho > 1:
        print("Você perdeu :(")
        print(" ")
        jogar_de_novo = str(input("Gostaria de jogar de novo? (digite s ou n): "))
        return jogar_de_novo
    else:
        print("Você ganhou!! :)")
        print(" ")
        jogar_de_novo = str(input("Gostaria de jogar de novo? (digite s ou n): "))
        return jogar_de_novo