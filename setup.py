'''Par crear paquetes distribuibles'''

from setuptools import setup

setup(
    name="paquetecalculo",
    version="1.0",
    description="Paquete redistribuible creado en el curso de pildorasinformaticas.",
    author="Óscar Flores",
    author_email="anscaryo@gmail.com",
    url="www.pildorasinformaticas.com",
    packages=["Calculo", "Calculo.basicas", "Calculo.redondeo_potencia"]
)
