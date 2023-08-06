


class Persona():
    def __init__(self, nombre, edad, residencia) -> None:
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}, tiene {self.edad} años, con residencia en {self.residencia}")


class Empleado(Persona):
    def __init__(self, salario, antiwedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiwedad

    def descripcion(self):
        super().descripcion()
        print(f"\tun salario de {self.salario}€ y una antigüedad de {self.antiguedad} años.")


antonio = Persona("Antonio", "35", "Sevilla")
antonio.descripcion()

manuel = Empleado(2500, 15, "Manuel", 55, "España")
manuel.descripcion()

print(isinstance(manuel, Empleado))
print(isinstance(manuel, Persona))
print(isinstance(antonio, Empleado))