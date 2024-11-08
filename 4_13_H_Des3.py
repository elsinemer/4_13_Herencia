class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def info(self):
        return f"'{self.titulo}' por {self.autor}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato, tamaño_archivo):
        # Inicializar atributos de la clase base Libro
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def info(self):
        # Mostrar información básica de Libro y los atributos adicionales de LibroDigital
        return (f"'{self.titulo}' por {self.autor}\n"
                f"Formato: {self.formato}\n"
                f"Tamaño de archivo: {self.tamaño_archivo} MB")

class EBook(LibroDigital):
    def __init__(self, titulo, autor, formato, tamaño_archivo, enlace_descarga):
        # Inicializar atributos de la clase base LibroDigital
        super().__init__(titulo, autor, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def info(self):
        # Mostrar información específica del EBook, incluyendo el enlace de descarga
        return (f"'{self.titulo}' por {self.autor}\n"
                f"Formato: {self.formato}\n"
                f"Tamaño de archivo: {self.tamaño_archivo} MB\n"
                f"Enlace de descarga: {self.enlace_descarga}")

# Crear una instancia de EBook y mostrar su información
ebook = EBook("El Principito", "Antoine de Saint-Exupéry", "EPUB", 1.5, "https://ejemplo.com/descarga/el_principito")
print(ebook.info())
