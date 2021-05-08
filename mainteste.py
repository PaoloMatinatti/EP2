import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final


baralho= baralho.cria_baralho()
print(baralho)
print(Lista_movimentos.lista_movimentos_possiveis(baralho,51))
carta=int(input('Escolha uma carta (digite um número entre 1 e 52): '))
carta=carta.possui_movimentos_possiveis_final
if carta not in possui_movimentos_possiveis_final():
    print('carta invalida, digite outro valor: ')

    