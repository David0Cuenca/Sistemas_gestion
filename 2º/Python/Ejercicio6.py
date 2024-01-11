import pickle

# Persona: Clase abstracta, contendrá el nombre, apellidos, DNI, etc.
class Persona:
    def __init__(self, Nombre, apellidos, DNI):
        self.Nombre = Nombre
        self.apellidos = apellidos
        self.DNI = DNI
        
    def __str__(self):
        return f"DNI: {self.DNI}, Nombre: {self.Nombre}, Apellidos: {self.apellidos}"

# Escuela: contendrá la información de las escuelas (nombre, localidad, responsable...).
class escuela:
    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesor = []
        self.alumnos = []
    def ShowAlumnos(self):
        for alumno in self.alumnos:
            print(f"Alumnos en el colegio {self.nombre}" + alumno.toString())
            
    def ShowProfesores(self):
            for profesor in self.profesor:
                print(f"Profesores en el colegio {self.nombre}" + profesor.toString())
                
    def __str__(self):
        return f"Nombre: {self.nombre}, localidad: {self.localidad}); responsable: {self.responsable}"
    

# Alumno (subclase de Persona): contendrá la información de los alumnos de la escuela (nombre, curso, profesor responsable (sólo uno)).
class Alumno(Persona):
    def __init__(self, Nombre, apellidos, DNI , Curso, Profesor_R):
        super().__init__(Nombre, apellidos, DNI)
        self.Curso = Curso
        self.Profesor_R = Profesor_R
        
    def __str__(self):
        return f"{super().__str__}, Curso: {self.Curso}, Profesor Responsable: {self.Profesor_R}"

# Profesor (subclase de Persona): contendrá información de los profesores que trabajan allí (nombre, tipos (ciencias, letras o mixto)).
class Profesor(Persona):
    def __init__(self, Nombre, apellidos, DNI, Tipos):
        super().__init__(Nombre, apellidos, DNI)
        self.Tipos = Tipos
        
    def __str__(self):
        return f"{super().__str__}, Tipos: {self.Tipos}"
    
# Menu principal
def MainMenu():
    print("1. Menu para los escuelas")
    print("2. Menu para los profesores")
    print("3. Menu para los alumnos")
    print("4. Salir")
    
    option = input("Seleccione una opción: ")
    MenuSelected(option)            

def MenuSelected(option):
    if option == "1":
        MenuEscuela()
    elif option == "2":
        MenuProfesor()
    elif option == "3":
        MenuAlumno()
    elif option == "4":
        MainMenu()
    else:
        print("Opción incorrecta")
        
def MenuEscuela():
    print("1. Crear escuela")
    print("2. Mostrar escuela")
    print("3. Salir")
    
    option = input("Seleccione una opción: ")
    if option == "1":
        nombre = input("Nombre de la escuela: ")
        localidad = input("Localidad de la escuela: ")
        responsable = input("Responsable de la escuela: ")
        createEscuela = escuela(nombre, localidad, responsable)
        MainMenu()
    elif option == "2":
        ExistEscuelas = CheckData()
        if ExistEscuelas:
            print(ExistEscuelas)
        else:
            print("No se hay escuelas registradas")
            MainMenu()
    elif option == "3":
        MainMenu()
        
def MenuProfesor():
    print("1. Crear profesor")
    print("2. Mostrar profesor")
    print("3. Salir")
    
    option = input("Seleccione una opción: ")
    if option == "1":
        nombre = input("Nombre del profesor: ")
        apellidos = input("Apellidos del profesor: ")
        dni = input("DNI del profesor: ")
        tipo = input("Tipo del profesor (Ciencias, Letras, Mixto): ")
        profesor_nuevo = Profesor(nombre, apellidos, dni, tipo)
        MainMenu()
    elif option == "2":
        ExistProfesores = CheckData()
        if ExistProfesores:
            print(ExistProfesores)
        else:
            print("No se hay profesores registrados")
            MainMenu()
    elif option == "3":
        MainMenu()

# # Persistencia de datos
# def guardar_datos(escuela):
#     with open('datos_escuela.pkl', 'wb') as file:
#         pickle.dump(escuela, file)

def CheckData():
    try:
        with open('datos_escuela.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# # Programa principal
# escuela_existente = cargar_datos()

# if escuela_existente:
#     escuela = escuela_existente
# else:
#     escuela = Escuela("Escuela Ejemplo", "Ciudad Ejemplo", "Responsable Ejemplo")

# while True:
#     mostrar_menu()
#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         nombre = input("Nombre del profesor: ")
#         apellidos = input("Apellidos del profesor: ")
#         dni = input("DNI del profesor: ")
#         tipo = input("Tipo del profesor (Ciencias, Letras, Mixto): ")
#         profesor_nuevo = Profesor(nombre, apellidos, dni, tipo)
#         escuela.agregar_profesor(profesor_nuevo)
#         print("Profesor agregado correctamente.")

#     elif opcion == "2":
#         print("Profesores:")
#         escuela.mostrar_profesores()

#     elif opcion == "3":
#         nombre = input("Nombre del alumno: ")
#         apellidos = input("Apellidos del alumno: ")
#         dni = input("DNI del alumno: ")
#         curso = input("Curso del alumno: ")
#         profesor_responsable = input("Profesor responsable del alumno: ")
#         alumno_nuevo = Alumno(nombre, apellidos, dni, curso, profesor_responsable)
#         escuela.agregar_alumno(alumno_nuevo)
#         print("Alumno agregado correctamente.")

#     elif opcion == "4":
#         print("Alumnos:")
#         escuela.mostrar_alumnos()

#     elif opcion == "5":
#         guardar_datos(escuela)
#         print("Saliendo del programa. ¡Hasta luego!")
#         break

#     else:
#         print("Opción no válida. Intente nuevamente.")
            


# #Datos de prueba
# Alumnos = Alumno("Digimom","Mamon","123456789","1º","Mamaracho")
# Alumnos.toString()