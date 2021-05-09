import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
import Empilha
import imprimirbaralho
baralho= baralho.cria_baralho()

test=True
print(imprimirbaralho.imprimir(baralho))
while test:
    c=1
    valor=int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))
    if valor > len(baralho)  :
        print('carta invalida')
    else:
        carta=baralho[valor-1]
    if possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho,valor) == True:
        if Lista_movimentos.lista_movimentos_possiveis(baralho,valor) == [1] :
            Empilha.empilha(baralho,valor,(valor-1))
 
        elif Lista_movimentos.lista_movimentos_possiveis(baralho,valor) ==[3]:
            Empilha.empilha(baralho,valor,(valor-3))
            imprimirbaralho.imprimir(baralho)

        elif Lista_movimentos.lista_movimentos_possiveis(baralho,valor) == [1,3]:
            esc=int(input('qual movimento deseja fazer:'))
            print('1.{}'.format(baralho[valor-1]))
            print('2. {}'.format(baralho[valor-3]))
            if esc == 1:
                Empilha.empilha(baralho,valor,(valor-1))
            else:
                 Empilha.empilha(baralho,valor,(valor-3))
    elif possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho,valor)== False:
        print('movimento invalido')
           

            
    if valor >= 53:
        a= 'Inválida'
        print('A carta é \033[31m{}\033[m'.format(a))
    else:
        carta=baralho[valor-1]
        print('\033[32m{}\033[m'.format(carta))
    
