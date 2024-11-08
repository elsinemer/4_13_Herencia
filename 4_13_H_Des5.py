class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def info_empleado(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario}"


class Voluntario:
    def __init__(self, nombre, horas_trabajadas):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas

    def info_voluntario(self):
        return f"Voluntario: {self.nombre}, Horas trabajadas: {self.horas_trabajadas}"


# Clase adicional de rol: Administrador
class Administrador:
    def __init__(self, seccion_responsable):
        self.seccion_responsable = seccion_responsable

    def responsabilidades(self):
        return f"Responsable de la sección: {self.seccion_responsable}"


# Clase adicional de rol: Mantenimiento
class Mantenimiento:
    def __init__(self, equipo):
        self.equipo = equipo

    def tareas_mantenimiento(self):
        return f"Mantenimiento del equipo: {self.equipo}"


# Clase Gerente que hereda de Empleado y usa composición con Administrador
class Gerente(Empleado):
    def __init__(self, nombre, salario, seccion_responsable):
        super().__init__(nombre, salario)
        # Composición: Un gerente también es administrador de una sección
        self.administrador = Administrador(seccion_responsable)

    def info_gerente(self):
        return (f"{self.info_empleado()}\n"
                f"{self.administrador.responsabilidades()}")


# Clase Tecnico que hereda de Empleado y usa composición con Mantenimiento
class Tecnico(Empleado):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        # Composición: Un técnico también realiza mantenimiento de equipo
        self.mantenimiento = Mantenimiento(equipo)

    def info_tecnico(self):
        return (f"{self.info_empleado()}\n"
                f"{self.mantenimiento.tareas_mantenimiento()}")


# Clase VoluntarioEspecializado que hereda de Voluntario y tiene el rol de Mantenimiento
class VoluntarioEspecializado(Voluntario):
    def __init__(self, nombre, horas_trabajadas, equipo):
        super().__init__(nombre, horas_trabajadas)
        # Composición: El voluntario también realiza tareas de mantenimiento
        self.mantenimiento = Mantenimiento(equipo)

    def info_voluntario_especializado(self):
        return (f"{self.info_voluntario()}\n"
                f"{self.mantenimiento.tareas_mantenimiento()}")


# Crear instancias y demostrar el uso de las clases
gerente = Gerente("Laura Sánchez", 5000, "Literatura")
tecnico = Tecnico("Carlos López", 3000, "Computadoras")
voluntario = Voluntario("Ana Pérez", 20)
voluntario_especializado = VoluntarioEspecializado("Luis González", 15, "Escáneres")

print(gerente.info_gerente())
print()
print(tecnico.info_tecnico())
print()
print(voluntario.info_voluntario())
print()
print(voluntario_especializado.info_voluntario_especializado())
