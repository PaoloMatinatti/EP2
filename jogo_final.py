import baralho
import movimentos
import ganhououperdeu

inicio = input("aperte ENTER para iniciar o jogo...")



fim_do_jogo = True
baralhos = baralho.cria_baralho()

while fim_do_jogo:

    baralhos = movimentos.movimentos(baralhos)
    acabou = ganhououperdeu.ganhou_ou_perdeu(baralhos)
    
<<<<<<< HEAD
    if fim_do_jogo == "s" or 'S':
        fim_do_jogo == True
        baralho = baralho.cria_baralho()
        
    elif fim_do_jogo == "n" or 'N': 
        fim_do_jogo == False
=======
    if acabou == False:
        fim_do_jogo= False
        
    else:
        baralhos = baralho.cria_baralho()

print ('Obrigado por jogar')
>>>>>>> 7bf2cb164d85d50a673fb851a5a4b4b1097500a6
