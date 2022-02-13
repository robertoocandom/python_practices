class herbie():

    def __init__(self):
        
        self.__largoChassis=230
        self.__anchoChassis=100
        self.__color='Blanco'
        self.__ruedas=4
        self.__motor='V4'
        self.__asientos='Tela'
        self.__estado_actual=True


    def avanzar(self, arrancamos):
        self.estado_actual=arrancamos
    


    def verificar_estado(self):
        if self.estado_actual == True:
            print(f'Tu Herbi tiene ', self.__ruedas, ' ruedas y esta detenido')
        else:
            print(f'Tu Herbi tiene ', self.__ruedas, ' ruedas y esta Avanzando')



print('** Primer Herbie creado **')
miherbie=herbie()
miherbie.avanzar(True)
print(miherbie.verificar_estado())


print('** Segundo Herbie creado **')cd 
miherbie2=herbie()
miherbie2.avanzar(False)
print(miherbie2.verificar_estado())




