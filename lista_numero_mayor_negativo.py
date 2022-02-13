num1 = int(input("Introduce numero positivos a sumar: "))
num2 = int(input("introduce otro numero para sumatoria: "))

while num1 and num2 >0:
    num1 = num1+num2
    num2 = int(input("introduce otro numero para sumatoria: "))

print('La sumatoria de los numeros es: ' + str(num1))

