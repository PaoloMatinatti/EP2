import baralho
import movimentos
import ganhououperdeu

inicio = input("aperte ENTER para iniciar o jogo...")



fim_do_jogo = True
baralhos = baralho.cria_baralho()

while fim_do_jogo:

    baralhos = movimentos.movimentos(baralhos)
    acabou = ganhououperdeu.ganhou_ou_perdeu(baralhos)
    
    if acabou == False:
        fim_do_jogo= False
        
    else:
        baralhos = baralho.cria_baralho()

print ('Obrigado por jogar')
