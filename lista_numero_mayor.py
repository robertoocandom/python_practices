
def verificar_lista(lista, numero):
    for i in lista:
        if i > numero:
            print('numero menor a los agregados')
            return False
    print('Numero Agregado')
    return True

def hacer_lista():
    lista_numero=[]
    continuar = True
    while continuar == True:
        numero = int(input('Introduce un numero que sea mayor al último : '))
        if verificar_lista(lista_numero, numero):
            lista_numero.append(numero)
            print(lista_numero)
        else:
            print('Tu lista de numeros es la siguiente')
            print(lista_numero)
            print('*** Fin del programa *** ')
            continuar=False


if __name__ == '__main__':
    print("**** Lista de numeros mayores ****")
    hacer_lista()
