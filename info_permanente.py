import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print('Se ha creado una persona nueva con el nombre: ', self.nombre )
   
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        listaDePersonas=open("FicheroExterno", "ab+")
        listaDePersonas.seek(0)
         
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)



    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("FicheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del Fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

milista=ListaPersonas()
persona=Persona("Fernanda", "Femenino", 29)
milista.agregarPersonas(persona)
milista.mostrarInfoFicheroExterno()





