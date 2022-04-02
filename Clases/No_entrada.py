def si_hay_correo_introducido(cadena):
    if cadena is None or cadena == '':
        print('No ha introducido ningun correo\nVuel')
        return True
    else:
        return False
