import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
import Empilha
import imprimirbaralho
baralho= baralho.cria_baralho()


print(imprimirbaralho.imprimir(baralho))
while possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho):
    c=1
    valor=int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))   
    if valor > len(baralho):
        a='Inválida'
        print('A carta é \033[31m{}\033[m'.format(a))
    else:
        carta=baralho[valor-1]

        print(carta)





    if possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho,valor) == True:
        if Lista_movimentos.lista_movimentos_possiveis(baralho,valor) ==[1]:
            Empilha.empilha(baralho,valor,(valor-1))
            print(imprimirbaralho.imprimir(baralho))
 
        elif Lista_movimentos.lista_movimentos_possiveis(baralho,valor) ==[3]:
            Empilha.empilha(baralho,valor,(valor-3))
            imprimirbaralho.imprimir(baralho)
            print(imprimirbaralho.imprimir(baralho))

        elif Lista_movimentos.lista_movimentos_possiveis(baralho,valor) == [1, 3]:
            print('1.{}'.format(baralho[valor-1]))
            print('2. {}'.format(baralho[valor-3]))
            esc=int(input('qual movimento deseja fazer:'))
            if esc == 1:
                Empilha.empilha(baralho,valor,(valor-1))
                print(imprimirbaralho.imprimir(baralho))
            else:
                 Empilha.empilha(baralho,valor,(valor-3))
                 print(imprimirbaralho.imprimir(baralho))
    elif possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho,valor)== False:
        b='Inválida'
        print('O movimento é \033[31m{}\033[m'.format(b))
           

            

    
