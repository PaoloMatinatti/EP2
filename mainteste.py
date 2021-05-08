import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
baralho= baralho.cria_baralho()
c=1
for item in baralho:
    print('{0}. {1}'.format(c,item))
    c+=1

valor=int(input('Escolha uma carta (digite um número entre 1 e 52): '))
carta=baralho[valor-1]
if valor >= 53:
    print('carta invalida')
print(carta)
