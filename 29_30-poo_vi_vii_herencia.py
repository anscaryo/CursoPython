class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frena(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca}\n\tModelo: {self.modelo}\n\tEn Marcha: {self.enmarcha}\n\tAcelerando: {self.acelera}\n\tFrenado: {self.frena}")


class V_Electrico(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True




class Moto(Vehiculos):
    hcaballito = "NO"

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito."
    ''' Sobre escritura de metodos'''
    def estado(self):
        print(f"Marca: {self.marca}\n\tModelo: {self.modelo}\n\tEn Marcha: {self.enmarcha}\n\tAcelerando: {self.acelera}\n\tFrenado: {self.frena}\n\t{self.hcaballito}")


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada."
        else:
            return "La furgoneta No esta cargada."


class BicicletaElectrica(V_Electrico, Vehiculos):
    pass





miMoto = Moto("Honda", "CBR")
miMoto.estado()
miMoto.acelerar()
miMoto.caballito()
miMoto.estado()


miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()

print(miFurgoneta.carga(True))

#miBici = BicicletaElectrica("Bh", "Electrica") #Al descomentar esta linea da error ya que
#                                               el orden de herencia es de izquierda a derecha
#                                               y el constructor de V_Electrica no admite parametros

miBici = BicicletaElectrica("BH", "Hibrid")
