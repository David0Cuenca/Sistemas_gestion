import json
import os
from tabnanny import check

# Persona: Clase abstracta, contendrá el nombre, apellidos, DNI, etc.
class Persona:
    def __init__(self, Nombre, apellidos, DNI):
        self.Nombre = Nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.escuela = None
        
    def __str__(self):
        return f"DNI: {self.DNI}, Nombre: {self.Nombre}, Apellidos: {self.apellidos}"

# Escuela: contendrá la información de las escuelas (nombre, localidad, responsable...).
class Escuela:
    def __init__(self, escuela_nombre, localidad, responsable):
        self.escuela_nombre = escuela_nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesores = []
        self.alumnos = []
    
    def ShowAlumnos(self):
        clear()
        if not self.alumnos:
            print(f"No hay alumnos en el colegio {self.escuela_nombre}")
        else:
            print(f"Alumnos en el colegio {self.escuela_nombre}")
            for alumno in self.alumnos:
                if alumno.escuela is None:
                    print(f"{alumno}")

    def ShowProfesores(self):
        clear()
        if not self.profesores:
            print(f"No hay profesores en el colegio {self.escuela_nombre}")
        else:
            print(f"Profesores en el colegio {self.escuela_nombre}")
            for profesor in self.profesores:
                if profesor.escuela is None:
                    print(f"{profesor}")
                    
    def ShowAll(self):
        clear()
        print(f"Profesores en el colegio {self.escuela_nombre}:")
        for profesor in self.profesores:
            print(f"{profesor}")
            
        print(f"Alumnos en el colegio {self.escuela_nombre}:")
        for alumno in self.alumnos:
            print(f"{alumno}")
    
    def add_profesores(self, profesor):
        self.profesores.append(profesor)
        
    def add_alumnos(self, alumno):
        self.alumnos.append(alumno)
        
    
    def __str__(self):
        return f"Nombre: {self.escuela_nombre}, localidad: {self.localidad}); responsable: {self.responsable}"
    

# Alumno (subclase de Persona): contendrá la información de los alumnos de la escuela (nombre, curso, profesor responsable (sólo uno)).

class Alumno(Persona):
    def __init__(self, Nombre, apellidos, DNI , Curso, Profesor_R):
        super().__init__(Nombre, apellidos, DNI)
        self.Curso = Curso
        self.Profesor_R = Profesor_R
        
    def __str__(self):
        return f"{super().__str__()}, Curso: {self.Curso}, Profesor Responsable: {self.Profesor_R}"

# Profesor (subclase de Persona): contendrá información de los profesores que trabajan allí (nombre, tipos (ciencias, letras o mixto)).

class Profesor(Persona):
    def __init__(self, Nombre, apellidos, DNI, Tipos):
        super().__init__(Nombre, apellidos, DNI)
        self.Tipos = Tipos
        
    def __str__(self):
        return f"{super().__str__}, Tipos: {self.Tipos}"
    
    
# Menu principal

def MainMenu():
    clear()
    DataEscuela = LoadData()
    
    if not DataEscuela:
        print("No hay ningun dato en la base de datos.")

    while True:
        print("1. Menu de escuelas")
        print("2. Crear profesor")
        print("3. Mostrar profesores")
        print("4. Crear alumno")
        print("5. Mostrar alumnos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            EscuelaMenu(DataEscuela)
        elif opcion == "2":
            CreateProfesor(None)  # None porque aún no hay una escuela asociada
        elif opcion == "3":
           ShowAllProfesores(DataEscuela)
        elif opcion == "4":
             CreateAlumno(None)# None porque aún no hay una escuela asociada
        elif opcion == "5":
            ShowAllAlumnos(DataEscuela)
        elif opcion == "6":
            print("Saliendo del programa.")
            exit()
        else:
            print("Opción incorrecta. Inténtelo de nuevo.")
            

def EscuelaMenu(DataEscuela):
    clear()
    while True:
        print("Escuelas disponibles, Seleccione la que quiere acceder:")
        for i, escuela in enumerate(DataEscuela, 0):
            print(f"{i+1}. {escuela.escuela_nombre}")
        print("A. Crear nueva escuela")
        print("B. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(DataEscuela):
                Select = DataEscuela[opcion - 1]
                Secundary_Menu(Select)
                break
            
        elif opcion.lower() == "a":
            CreateEscuela()
            break
        
        elif opcion.lower() == "b":
            MainMenu()
        else:
            print("Opción incorrecta. Inténtelo de nuevo.")

#Selector para las gestionar todas las entidades

def Secundary_Menu(Selected_Escuela):

    options ={
        "1": Selected_Escuela.ShowAll,
        "2": lambda: AssignProfesorToEscuela(Selected_Escuela),
        "3": lambda: AssignAlumnoToEscuela(Selected_Escuela),
        "4": lambda: EliminateProfesores(Selected_Escuela),
        "5": lambda: EliminateAlumnos(Selected_Escuela),
        "6": lambda: EliminateEscuela(Selected_Escuela),
        "7": MainMenu
    }

    while True:
        print(f"Escuela seleccionada: {Selected_Escuela.nombre}")
        print("----------------------------------")
        print("1. Mostrar todo")
        print("2. Añadir profesor")
        print("3. Añadir alumno")
        print("4. Eliminar profesor")
        print("5. Eliminar alumno")
        print("6. Eliminar esta escuela")
        print("7. Atrás")

        opcion = input("Seleccione una opción: ")
        if opcion in options:
            options[opcion]()
        else:
            print("Opción incorrecta. Inténtelo de nuevo.")
        

def CreateEscuela():
    clear()
    nombre = input("Nombre de la escuela: ")
    localidad = input("Localidad de la escuela: ")
    responsable = input("Responsable de la escuela: ")
    
    createEscuela = Escuela(nombre, localidad, responsable)
    SaveData(createEscuela)
    MainMenu()
    
    
def CreateProfesor(Selected):
    clear()
    nombre = input("Nombre del profesor: ")
    apellidos = input("Apellidos del profesor: ")
    dni = input("DNI del profesor: ")
    tipo = input("Tipo del profesor (Ciencias, Letras, Mixto): ")
    
    createProfesor = Profesor(nombre, apellidos, dni, tipo)
    
    
    SaveData(createProfesor)


def CreateAlumno(Selected):
    clear()
    nombre = input("Nombre del alumno: ")
    apellidos = input("Apellidos del alumno: ")
    dni = input("DNI del alumno: ")
    curso = input("Curso del alumno: ")
    profesor_r = input("Profesor responsable del alumno: ")
    
    alumno_nuevo = Alumno(nombre, apellidos, dni, curso, profesor_r)
    
    SaveData(alumno_nuevo)
    
    
def EliminateAlumnos(Selected):
    if Selected.alumnos == []:
        print("No hay alumnos en esta escuela.")
        return
    else:
        while True:
            opcion = input("Seleccione un alumno a eliminar (número): ")
            if opcion.isdigit():
                opcion = int(opcion)
                if 1 <= opcion <= len(Selected.alumnos):
                    alumno_eliminar = Selected.alumnos[opcion - 1]
                    Selected.alumnos.remove(alumno_eliminar)
                    SaveData(Selected)
                    break
            print("Opción incorrecta. Inténtelo de nuevo.")

def EliminateProfesores(Selected):
    if Selected.profesores == []:
        print("No hay profesores en esta escuela.")
        return
    else:
        while True:
            opcion = input("Seleccione un profesor a eliminar (número): ")
            if opcion.isdigit():
                opcion = int(opcion)
                if 1 <= opcion <= len(Selected.profesores):
                    profesor_eliminar = Selected.profesores[opcion - 1]
                    Selected.profesores.remove(profesor_eliminar)
                    SaveData(Selected)
                    break
            print("Opción incorrecta. Inténtelo de nuevo.")

        
def EliminateEscuela(Selected):
    option = input("Seguro que desea eliminar el profesor? (S/N): ")
    if option.lower() == "s":
        DataEscuela = LoadData()
        DataEscuela.remove(Selected)
        SaveData(DataEscuela)
        print(f"Escuela {Selected.nombre} eliminada.")
    else:
        print(f"No se eliminó la escuela {Selected.escuela_nombre}.")
        
def ShowAllProfesores(DataEscuela):
    clear()
    print("Profesores en todas las escuelas:")
    for escuela in DataEscuela:
        for profesor in escuela.profesores:
            print(f"{profesor}")

def ShowAllAlumnos(DataEscuela):
    clear()
    print("Alumnos en todas las escuelas:")
    for escuela in DataEscuela:
        for alumno in escuela.alumnos:
            print(f"{alumno}")


def ShowUnassignedAlumnos():
    unassigned_alumnos = [alumno for escuela in LoadData() if isinstance(escuela, Escuela) for alumno in escuela.alumnos if alumno.escuela is None]
    
    if not unassigned_alumnos:
        print("No hay alumnos sin escuela asociada.")
    else:
        print("Alumnos sin escuela asociada:")
        for i, alumno in enumerate(unassigned_alumnos, 1):
            print(f"{i}. {alumno}")

def ShowUnassignedProfesores():
    unassigned_profesores = [profesor for escuela in LoadData() if isinstance(escuela, Escuela) for profesor in escuela.profesores if profesor.escuela is None]
    
    if not unassigned_profesores:
        print("No hay profesores sin escuela asociada.")
    else:
        print("Profesores sin escuela asociada:")
        for i, profesor in enumerate(unassigned_profesores, 1):
            print(f"{i}. {profesor}")

def AssignAlumnoToEscuela(Selected):
    ShowUnassignedAlumnos()

    try:
        opcion = int(input("Seleccione un alumno para añadir a la escuela (número): "))
        unassigned_alumnos = [alumno for escuela in LoadData() if isinstance(escuela, Escuela) for alumno in escuela.alumnos if alumno.escuela is None]

        if 1 <= opcion <= len(unassigned_alumnos):
            selected_alumno = unassigned_alumnos[opcion - 1]
            selected_alumno.escuela = Selected
            Selected.alumnos.append(selected_alumno)
            SaveData(Selected)
            print(f"Alumno {selected_alumno.Nombre} añadido a la escuela {Selected.escuela_nombre}.")
        else:
            print("Opción incorrecta.")
    except ValueError:
        print("Ingrese un número válido.")

def AssignProfesorToEscuela(Selected):
    ShowUnassignedProfesores()

    try:
        opcion = int(input("Seleccione un profesor para añadir a la escuela (número): "))
        unassigned_profesores = [profesor for escuela in LoadData() if isinstance(escuela, Escuela) for profesor in escuela.profesores if profesor.escuela is None]

        if 1 <= opcion <= len(unassigned_profesores):
            selected_profesor = unassigned_profesores[opcion - 1]
            selected_profesor.escuela = Selected
            Selected.profesores.append(selected_profesor)
            SaveData(Selected)
            print(f"Profesor {selected_profesor.Nombre} añadido a la escuela {Selected.escuela_nombre}.")
        else:
            print("Opción incorrecta.")
    except ValueError:
        print("Ingrese un número válido.")



def SaveData(data):
    existing_data = LoadData()

    if isinstance(existing_data, list):
        existing_data.append(data)
    else:
        existing_data = [existing_data, data]

    with open('datos_escuela.json', 'w') as file:
        json.dump(existing_data, file, default=lambda obj: obj.__dict__)


def LoadData():
    try:
        with open('datos_escuela.json', 'r') as file:
            data = json.load(file)
            return [json_to_obj(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        with open('datos_escuela.json', 'w') as file:
            json.dump([], file)
        return []

def json_to_obj(json_data):
    if 'escuela_nombre' in json_data:
        escuela = Escuela(json_data.get('escuela_nombre', ''), json_data.get('localidad', ''), json_data.get('responsable', ''))
        escuela.profesores = [json_to_obj(profesor) for profesor in json_data.get('profesores', [])]
        escuela.alumnos = [json_to_obj(alumno) for alumno in json_data.get('alumnos', [])]
        return escuela
    elif 'alumno_nombre' in json_data:
        return Alumno(
            json_data.get('alumno_nombre', ''),
            json_data.get('apellidos', ''),
            json_data.get('DNI', ''),
            json_data.get('Curso', ''),
            json_data.get('Profesor_R', '')
        )
    else:
        return Profesor(
            json_data.get('profesor_nombre', ''),
            json_data.get('apellidos', ''),
            json_data.get('DNI', ''),
            json_data.get('Tipos', '')
        )

def obj_to_json(obj):
    if isinstance(obj, Escuela):
        return {
            'escuela_nombre': obj.escuela_nombre,
            'localidad': obj.localidad,
            'responsable': obj.responsable,
            'profesores': [obj_to_json(profesor) for profesor in obj.profesores],
            'alumnos': [obj_to_json(alumno) for alumno in obj.alumnos]
        }
    elif isinstance(obj, Alumno):
        return {
            'alumno_nombre': obj.Nombre,
            'apellidos': obj.apellidos,
            'DNI': obj.DNI,
            'Curso': obj.Curso,
            'Profesor_R': obj.Profesor_R
        }
    elif isinstance(obj, Profesor):
        return {
            'profesor_nombre': obj.Nombre,
            'apellidos': obj.apellidos,
            'DNI': obj.DNI,
            'Tipos': obj.Tipos
        }

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

MainMenu()