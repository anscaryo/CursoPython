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

class Moto(Vehiculos):
    pass

miMoto = Moto("Honda", "CBR")
miMoto.estado()
miMoto.acelerar()
miMoto.estado()