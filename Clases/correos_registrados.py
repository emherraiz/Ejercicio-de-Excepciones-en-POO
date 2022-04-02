class Registro:
    def __init__(self, lista_de_correos, eliminado = None, añadido = None):
        self.correos = lista_de_correos
        self.eliminado = eliminado
        self.añadido = añadido

    def mostrar_correos(self):
        for i in range(len(self.correos)):
            print(f'{i+1} - {self.correos}')

    def devolver_correos(self):
        return self.correos

    def eliminar_correo(self):
        # Se puede hacer una herencia pasando una clase con funciones que me permitan editar una lista
        return self.correos.remove(self.eliminar)

    def añadir_correo(self):
        return self.correos.append(self.añadido)
