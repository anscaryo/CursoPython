import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(
            f"Se ha dado de alta una persona nueva con el nombre de {self.nombre}")

    def __str__(self) -> str:
        return "Nombre: {}\n\tGenero: {}\n\tEdad: {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del ficheros externo".format(
                len(self.personas)))
        except:
            print("El fichero esta vacio.")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close
        del (listaDePersonas)

    def mostrarInfoExterno(self):
        print("La información del fichero externo es:")
        for p in self.personas:
            print(p)


miLista = ListaPersonas()

p = Persona("Mamen", "Femenino", 29)
miLista.agregarPersonas(p)
p = Persona("Óscar", "Masculino", 29)
miLista.agregarPersonas(p)
miLista.mostrarInfoExterno()
# p = Persona("Antonio", "Masculino", 39)
# miLista.agregarPersonas(p)
# p = Persona("Pedro", "Masculino", 45)
# miLista.agregarPersonas(p)
# p = Persona("Yolanda", "Femenino", 35)
# miLista.agregarPersonas(p)
# p = Persona("Maria", "Femenino", 19)
# miLista.agregarPersonas(p)
# p = Persona("Manuel", "Masculino", 43)
# miLista.agregarPersonas(p)

# miLista.mostrarPersonas()
