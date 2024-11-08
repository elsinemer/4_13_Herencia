class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def info_usuario(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

class Bibliotecario(Usuario):
    def __init__(self, nombre, id_usuario, seccion, años_experiencia):
        # Inicializar los atributos de la clase base Usuario
        super().__init__(nombre, id_usuario)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def info_bibliotecario(self):
        # Devuelve una descripción detallada del bibliotecario
        return (f"{self.nombre} es el bibliotecario de la sección {self.seccion} con "
                f"{self.años_experiencia} años de experiencia.")

# Crear una instancia de Bibliotecario y mostrar su información
bibliotecario = Bibliotecario("Ana Gómez", "B123", "Literatura", 5)
print(bibliotecario.info_usuario())  # Muestra información básica del usuario
print(bibliotecario.info_bibliotecario())  # Muestra información específica del bibliotecario
