def retorna_maior_valor(lista):

    maior_numero = lista[0]

    for i in lista:
        if i > maior_numero:
            maior_numero = i

    return maior_numero

def retorna_menor_valor(lista):

    menor_numero = lista[0]

    for i in lista:
        if i < menor_numero:
            menor_numero = i

    return menor_numero

print(retorna_maior_valor((1, 2, 30, 4, 5, 6)))

print(retorna_menor_valor([10, 2, 30, 4, 5, 1]))