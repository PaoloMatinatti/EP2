#jogo finalizado 
import baralho
import movimentos
import ganhououperdeu
print('''
Paciência Acordeão 
================== 

Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 

Existem apenas dois movimentos possíveis: 

1. Empilhar uma carta sobre a carta imediatamente anterior; 
2. Empilhar uma carta sobre a terceira carta anterior. 

Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

1. As duas cartas possuem o mesmo valor ou 
2. As duas cartas possuem o mesmo naipe. 

Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

''')
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


