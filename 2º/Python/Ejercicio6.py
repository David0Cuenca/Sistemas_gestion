class Persona:
    def __init__(self, Nombre, apellidos, DNI):
        self.Nombre = Nombre
        self.apellidos = apellidos
        self.DNI = DNI
        
    def toString(self):
        return f"DNI: {self.DNI}, Nombre: {self.Nombre}, Apellidos: {self.apellidos}"

class escuela:
    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesor = []
        self.alumnos = []
    def toString(self):
        return f"Nombre: {self.nombre},  "    

class Alumno(Persona):
    def __init__(self, Nombre, apellidos, DNI , Curso, Profesor_R):
        super().__init__(Nombre, apellidos, DNI)
        self.Curso = Curso
        self.Profesor_R = Profesor_R
        
    def toString(self):
        return f"{super().toString()}, Curso: {self.Curso}, Profesor Responsable: {self.Profesor_R}"
    
#Datos de prueba
Alumnos = Alumno("Digimom","Mamon","123456789","1º","Mamaracho")
Alumnos.toString()