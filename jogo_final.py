import baralho
import movimentos
import ganhououperdeu

inicio = input("aperte ENTER para iniciar o jogo...")



fim_do_jogo = True
baralho = baralho.cria_baralho()

while fim_do_jogo:

    baralho = movimentos.movimentos(baralho)
    fim_do_jogo = ganhououperdeu.ganhou_ou_perdeu(baralho)
    
    if fim_do_jogo == "s":
        fim_do_jogo == True
        baralho = baralho.cria_baralho()
        
    elif fim_do_jogo == "n":
        fim_do_jogo == False
