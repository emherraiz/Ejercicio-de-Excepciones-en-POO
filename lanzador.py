import sys
from Clases.No_entrada import *
from Clases.Mal_formateado import *
from Clases.no_registrado import *

class Introduce_algun_correo(BaseException):
    def __str__(self):
        return 'No se ha introducido ningun correo'

class Prueba_otro_correo(BaseException):
    def __init__(self, cadena):
        self.cadena = cadena

    def __str__(self):
        return f'{self.cadena} no tiene el formato de un correo electronico'

class No_esta_en_la_base(BaseException):
    def __init__(self, cadena):
        self.cadena = cadena

    def __str__(self):
        return f'El correo {self.cadena} no existe'

def correo_correcto(cadena):
    if No_hay_correo_introducido(cadena):
        raise Introduce_algun_correo(cadena)
    elif formato_incorrecto(cadena):
        raise Prueba_otro_correo(cadena)
    elif registro(cadena):
        raise No_esta_en_la_base(cadena)

cadena = input('Introduce un correo:')
correo_correcto(cadena)

