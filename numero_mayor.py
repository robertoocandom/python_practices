
def evalua_numeros(num1, num2):
    if num1 > num2:
        print(f"El primero numero {num1} es mayor que el segundo {num2}")
    elif num2 > num1:
        print(f"El segundo numero {num2} es mayor que el primero {num1}")
    else:
        print("Ambos numeros son iguales")
    

print('Comparacion de Numeros enteros')
num1 = int(input('Introduce el primer numero entero a comprar: '))
num2 = int(input('Introduce el segundo numero entero a comprar: '))

evalua_numeros(num1, num2)

print('*** Fin del Programa ***')