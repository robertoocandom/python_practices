print('Programa de Validación de Email - Ejercicio')

the_email = input('Introducir el email a Validar: ')
contador = 0

for i in the_email:
    if i == '@' or i == '.':
        # print(i, contador)
        contador = contador + 1

if contador == 2:
    print(f'El email {the_email} es valido')
else:
    print(f'El email {the_email} es invalido')

print('Termino el Programa')



