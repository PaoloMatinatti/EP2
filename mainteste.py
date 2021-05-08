import baralho
import Lista_movimentos
import possui_movimentos_possiveis_final
baralho= baralho.cria_baralho()
print(baralho)
print(Lista_movimentos.lista_movimentos_possiveis(baralho,51))
if possui_movimentos_possiveis_final.possui_movimentos_possiveis(baralho,51)== True:
    print('teste')
else:
    print('teste2')
