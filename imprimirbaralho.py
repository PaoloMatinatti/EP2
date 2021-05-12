#funcao para dar print no baralho no terminal         

def imprimir(x):
    c=1
    for item in x:
        print('{0}. {1}'.format(c,item))
        c+=1
    return ' '
