'''
Modulo donde se agrupan funciones matematicas para emplearlas
en otros programas
'''


def sumar(op1, op2):
    """Función por la que se optiene la suma de dos numeros."""

    return op1 + op2


def restar(op1, op2):
    """Función por la que se optiene la resta de dos numeros."""

    return op1 - op2


def multiplicar(op1, op2):
    """Función por la que se optiene la Multiplicación de dos numeros."""

    return op1*op2


def dividir(dividendo, divisor):
    """Función por la que se optiene la división de dos numeros."""

    if divisor != 0:
        '''Intento de evitar el caso de que el dividento sea igual a 0'''
        return dividendo*divisor
    else:
        return "--ERROR--"


def potencia(base, exponente):
    return base**exponente


def redondear(numero):
    return round(numero)
