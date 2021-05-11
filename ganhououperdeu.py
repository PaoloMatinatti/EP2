def ganhou_ou_perdeu(baralho):
    if len(baralho) > 1:
        a='perdeu'
        print("Você \033[031m{}\033[m".format(a))
        print(" ")     
    else:
        b='Ganhou'
        print("Você \033[32m{}\033[m".format(b))
        print(" ")
    tt= True
    while tt:
        fim = input('deseja jogar novamente? (digite s/S ou  n/N): ')
        if fim == 'n' or 'N' :
            return False
            tt= False
        elif fim == 's' or 'S' :
            return True
            tt= False
        elif fim != 'n' or 'N' and fim != 's' or 'S' :
            print('movimento invalido')
   
