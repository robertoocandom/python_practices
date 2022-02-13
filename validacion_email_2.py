email=input('Introduce un email: ')

while True:
    contar=email.count("@")
    print('primer:', email.find('@'))
    print('ultimo:', email.rfind('@'))
    print(len(email)-1)

    if contar!=1:
        print('Email debe tener un solo @')
    elif email.find('@') == 0:
        print('Email no Valido: El primer caracter no debe ser un @')
    elif email.rfind('@')==(len(email)-1) :
        print('Email No Valido: El Ultimo caracter no debe ser un @')
    else:
        print(f'El email {email} es Valido') 
    break
