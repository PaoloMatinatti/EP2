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
        a= 'Inválida'
        print('A carta é \033[31m{}\033[m'.format(a))
    else:
        carta=baralho[valor-1]
        print('\033[32m{}\033[m'.format(carta))
    
