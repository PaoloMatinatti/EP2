import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
baralho= baralho.cria_baralho()
print(baralho)
print(Lista_movimentos.lista_movimentos_possiveis(baralho,51))
valor=int(input('Escolha uma carta (digite um número entre 1 e 52): '))
carta=baralho[valor-1]
if valor >= 53:
    print('carta invalida')
print(carta)