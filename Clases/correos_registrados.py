import os
class Registro:
    def __init__(self, correos):
        self.correos = correos

    def mostrar_correos(self):
        for i in range(len(self.correos)):
            print(f'{i+1} - {self.correos[i]}')

    def devolver_correos(self):
        return self.correos

    def eliminar_correo(self, eliminado):
        # Se puede hacer una herencia pasando una clase con funciones que me permitan editar una lista
        # De momento estas funciones no las voy a usar
        return self.correos.remove(eliminado)

    def añadir_correo(self, añadido):
        return self.correos.append(añadido)

correos = ['quiquemh2001@gmail.com', 'eherreiz@outlook.com', 'eherraiz@outlook.com']
modificar_registro = Registro(correos)
# Por ahora no se tratar con bases de datos asi que me reduzco a una simple lista
opciones = '\n1 - Mostrar correos\n2 - Añadir correo\n3 - Eliminar correo\n4 - No la lista de correos permanece inalterada'
continuar = True
while continuar == True:
    print(opciones)
    opcion = int(input('\n\nDesea realizar alguna opcion antes de comprobar si el registro corresponde con la base de datos:\n'))
    if opcion == 1:
        print('Nuestros correos son los siguientes\n')
        modificar_registro.mostrar_correos()
    elif opcion == 2:
        # Aqui tendriamos que comprobar si el correo que añadimos es
        añadido = input('Añade tu correo:\n')
        modificar_registro.añadir_correo(añadido)
    elif opcion == 3:
        eliminado = input('Correo que quiere eliminar:\n')
        modificar_registro.eliminar_correo(eliminado)
    elif opcion == 4:
        continuar = False
    else:
        print('Introduzca una opcion correcta')




correos_registrados = modificar_registro.devolver_correos()
