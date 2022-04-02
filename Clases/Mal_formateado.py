import re
def formato_incorrecto(cadena):
    if re.search(".*@.*\..*", cadena) is None:
        return True
    else:
        return False
