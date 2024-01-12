import json
import os
from tabnanny import check
from tkinter.tix import Select
from numpy import save

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
        self.profesores = []
        self.alumnos = []
        
    def get_Profesores(self):
        return self.alumnos
            
    def get_Alumnos(self):
        return self.profesores
    
    def ShowAlumnos(self):
        for alumno in self.alumnos:
            print(f"Alumnos en el colegio {self.nombre}" + alumno.toString())

    def ShowProfesores(self):
        for profesor in self.profesores:
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
    DataEscuela = CheckData()
    
    if not CheckData():
        print("No hay escuelas registradas. Vamos a registrar una nueva.")
        CreateEscuela()

    print("Escuelas disponibles:")
    for i, escuela in enumerate(DataEscuela, 0):
        print(f"{i+1}. {escuela['nombre']}")

    while True:
        opcion = input("Seleccione una escuela existente (número): ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(DataEscuela):
                Select = DataEscuela[opcion - 1]
                Secundary_Menu(Select)
                break
        print("Opción incorrecta. Inténtelo de nuevo.")      

#Selector para las gestionar todas las entidades

def Secundary_Menu(Select):

    while True:
        clear()
        print(f"Escuela seleccionada: {Select['nombre']}")
        print("----------------------------------")
        print("1. Añadir profesor")
        print("2. Añadir alumno")
        print("3. Mostrar profesores")
        print("4. Mostrar alumnos")
        print("5. Atrás")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            CreateProfesor(Select)
        elif opcion == "2":
            CreateAlumno(Select)
        elif opcion == "3":
            Select.ShowProfesor()
        elif opcion == "4":
            Select.ShowAlumno()
        elif opcion == "5":
            exit()
        else:
            print("Opción incorrecta. Inténtelo de nuevo.")

def CreateEscuela():
    nombre = input("Nombre de la escuela: ")
    localidad = input("Localidad de la escuela: ")
    responsable = input("Responsable de la escuela: ")
    createEscuela = escuela(nombre, localidad, responsable)
    SaveData(createEscuela)
    
def CreateProfesor(Selected):
    nombre = input("Nombre del profesor: ")
    apellidos = input("Apellidos del profesor: ")
    dni = input("DNI del profesor: ")
    tipo = input("Tipo del profesor (Ciencias, Letras, Mixto): ")
    createProfesor = Profesor(nombre, apellidos, dni, tipo)
    Selected.profesor.append(createProfesor)
    SaveData(Selected)

def CreateAlumno(Selected):
    nombre = input("Nombre del alumno: ")
    apellidos = input("Apellidos del alumno: ")
    dni = input("DNI del alumno: ")
    curso = input("Curso del alumno: ")
    profesor_r = input("Profesor responsable del alumno: ")
    alumno_nuevo = Alumno(nombre, apellidos, dni, curso, profesor_r)
    Selected.alumnos.append(alumno_nuevo)
    SaveData(Selected)
    
              
def SaveData(data):
    existing_data = CheckData()
    existing_data.append(data)
    
    try:
        with open('datos_escuela.json', 'r') as file:
            existing_data = json.load(file)
        if isinstance(existing_data, list):
            existing_data.append(data)
        else:
            existing_data = [existing_data, data]
    except FileNotFoundError:
        existing_data = [data]

    with open('datos_escuela.json', 'w') as file:
        json.dump(existing_data, file, default=lambda obj: obj.__dict__)

def CheckData():
    try:
        with open('datos_escuela.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
MainMenu()