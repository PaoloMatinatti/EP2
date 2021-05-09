import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
import Empilha
import imprimirbaralho
baralho= baralho.cria_baralho()


while possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho):
    x = imprimirbaralho.imprimir(baralho)
    valor=int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))   
    while valor > len(baralho):
        a='Inválida'
        valor=int(input('A carta é \033[31m{}\033[m selecione outra: '.format(a)))
    indice= valor-1
    movimentos= Lista_movimentos.lista_movimentos_possiveis(baralho,indice)
    if len(movimentos) == 2:
        print('qual movimento deseja fazer?')
        print('1. {}'.format(baralho[indice-1]))
        print('2. {}'.format(baralho[indice-3]))
        esq= int(input('escolha ou 1 ou 2: '))

        if esq == 1:
            baralho[indice-1] = baralho[indice]
            del baralho[indice]
        elif esq == 2:
            baralho[indice-3] = baralho[indice]
            del baralho[indice]
    else:
        for i in movimentos:
            if i == 1:
                baralho= Empilha.empilha(baralho,indice,indice-1)
                print(len(baralho))
            elif i == 3:
                baralho= Empilha.empilha(baralho,indice,indice-3)
                print(len(baralho))
        else:
            input('movimento invalido')
    









            

    
