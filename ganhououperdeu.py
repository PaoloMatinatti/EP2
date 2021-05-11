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
        fim = input('deseja jogar novamente? (digite s ou  n): ')
        if fim == 'n' :
            return False
            tt= False
        elif fim == 's' :
            return True
            tt= False
        elif fim != 'n' and fim != 's' :
            print('movimento invalido')
   
