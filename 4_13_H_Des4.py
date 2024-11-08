class Escritor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def biografia(self):
        return f"{self.nombre} es un escritor de nacionalidad {self.nacionalidad}."

class Academico:
    def __init__(self, institucion, especialidad):
        self.institucion = institucion
        self.especialidad = especialidad

    def info_academica(self):
        return f"Trabaja en {self.institucion} como especialista en {self.especialidad}."

class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, nacionalidad, institucion, especialidad):
        # Inicializar ambas clases base utilizando super() en herencia múltiple
        super().__init__(nombre, nacionalidad)
        Academico.__init__(self, institucion, especialidad)  # Llamada explícita para Academico

    def biografia(self):
        # Sobrescribe el método para incluir información académica
        return (f"{self.nombre} es un escritor y académico de nacionalidad {self.nacionalidad}.\n"
                f"Especialista en {self.especialidad} en {self.institucion}.")

    def publicar_articulo(self, titulo, revista):
        return f"{self.nombre} ha publicado un artículo titulado '{titulo}' en la revista '{revista}'."

# Crear una instancia de EscritorAcademico y demostrar el funcionamiento de sus métodos
escritor_academico = EscritorAcademico("Juan Pérez", "mexicana", "Universidad Nacional", "Literatura Comparada")
print(escritor_academico.biografia())
print(escritor_academico.info_academica())
print(escritor_academico.publicar_articulo("La narrativa moderna", "Revista de Estudios Literarios"))
