from correos_registrados import *
def registro(cadena):
    if cadena in correos_registrados:
        return True
    else:
        return False

