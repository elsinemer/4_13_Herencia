class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def biografia(self):
        return f"{self.nombre} es un autor de nacionalidad {self.nacionalidad}."

class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Inicializar atributos de la clase base Autor
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

    def biografia(self):
        # Sobrescribimos el método para incluir el tipo de poesía
        return f"{self.nombre} es un poeta de nacionalidad {self.nacionalidad}, especializado en poesía {self.tipo_poesia}."

# Crear una instancia de Poeta y mostrar su información
poeta = Poeta("Pablo Neruda", "chilena", "lírica")
print(poeta.biografia())
