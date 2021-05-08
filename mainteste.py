import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
baralho= baralho.cria_baralho()
c=1
for item in baralho:
    print('{0}. {1}'.format(c,item))
    c+=1
c=1
test=True
while test:
    valor=int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))
    if valor >= 53:
        print('carta invalida')
    else:
        carta=baralho[valor-1]
        print(carta)
    
