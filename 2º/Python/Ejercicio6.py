import json
import os
from tabnanny import check

# Persona: Clase abstracta, contendrá el nombre, apellidos, DNI, etc.
class Persona:
    def __init__(self, Nombre, apellidos, DNI):
        self.Nombre = Nombre
        self.apellidos = apellidos
        self.DNI = DNI
        
    def __str__(self):
        return f"DNI: {self.DNI}, Nombre: {self.Nombre}, Apellidos: {self.apellidos}"

# Escuela: contendrá la información de las escuelas (nombre, localidad, responsable...).
class Escuela:
    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesores = []
        self.alumnos = []
    
    def ShowAlumnos(self):
        clear()
        if not self.alumnos:
            print(f"No hay alumnos en el colegio {self.nombre}")
        else:
            print(f"Alumnos en el colegio {self.nombre}:")
            for alumno in self.alumnos:
                print(f"{alumno}")

    def ShowProfesores(self):
        clear()
        if not self.profesores:
            print(f"No hay profesores en el colegio {self.nombre}")
        else:
            print(f"Profesores en el colegio {self.nombre}:")
            for profesor in self.profesores:
                print(f"Profesores en el colegio {self.nombre}: {profesor}")
    
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
    clear()
    DataEscuela = LoadData()
    
    if not DataEscuela:
        print("No hay escuelas registradas. Vamos a registrar una nueva.")
        CreateEscuela()

    print("Escuelas disponibles:")
    for i, escuela in enumerate(DataEscuela, 0):
        print(f"{i+1}. {escuela.nombre}")
    while True:
        opcion = input("Seleccione una escuela existente (número) o pulse N para crear una nueva escuela: ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(DataEscuela):
                Select = DataEscuela[opcion - 1]
                Secundary_Menu(Select)
                break
        elif opcion == "n" or opcion == "N":
            CreateEscuela()
            break
        else:
            print("Opción incorrecta. Inténtelo de nuevo.")      

#Selector para las gestionar todas las entidades

def Secundary_Menu(Select_Escuela):

    options ={
        "1": lambda: CreateProfesor(Select_Escuela),
        "2": lambda: CreateAlumno(Select_Escuela),
        "3": Select_Escuela.ShowProfesores,
        "4": Select_Escuela.ShowAlumnos,
        "5": lambda: EliminateProfesores(Select_Escuela),
        "6": lambda: EliminateAlumnos(Select_Escuela),
        "7": lambda: EliminateEscuela(Select_Escuela),
        "8": MainMenu
    }

    while True:
        print(f"Escuela seleccionada: {Select_Escuela.nombre}")
        print("----------------------------------")
        print("1. Añadir profesor")
        print("2. Añadir alumno")
        print("3. Mostrar profesores")
        print("4. Mostrar alumnos")
        print("5. Eliminar profesor")
        print("6. Eliminar alumno")
        print("7. Eliminar esta escuela")
        print("8. Atrás")

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
    Selected.profesores.append(createProfesor)
    SaveData(Selected)


def CreateAlumno(Selected):
    clear()
    nombre = input("Nombre del alumno: ")
    apellidos = input("Apellidos del alumno: ")
    dni = input("DNI del alumno: ")
    curso = input("Curso del alumno: ")
    profesor_r = input("Profesor responsable del alumno: ")
    alumno_nuevo = Alumno(nombre, apellidos, dni, curso, profesor_r)
    Selected.alumnos.append(alumno_nuevo)
    SaveData(Selected)
    
    
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
    if option == "S" or option == "s":
        DataEscuela = LoadData()
        DataEscuela.remove(Selected)
        SaveData(DataEscuela)
        print(f"Escuela {Selected.nombre} eliminada.")
    else:
        print(f"No se eliminó la escuela {Selected.nombre}.")
        

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
    escuela = Escuela(json_data.get('nombre', ''), json_data.get('localidad', ''), json_data.get('responsable', ''))
    escuela.profesores = [json_to_obj(profesor) for profesor in json_data.get('profesores', [])]
    escuela.alumnos = [json_to_obj(alumno) for alumno in json_data.get('alumnos', [])]
    return escuela



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

MainMenu()