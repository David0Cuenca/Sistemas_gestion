import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class School:
    def __init__(self, name, location, responsible):
        self.name = name
        self.location = location
        self.responsible = responsible
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def remove_teacher(self, teacher):
        self.teachers.remove(teacher)

    def remove_student(self, student):
        self.students.remove(student)

    def show_teachers(self):
        if not self.teachers:
            print("No hay profesores en esta escuela.")
        for teacher in self.teachers:
            print(teacher, f"Escuela: {self.name}")

    def show_students(self):
        if not self.students:
            print("No hay alumnos en esta escuela.")
        for student in self.students:
            print(student, f"Escuela: {self.name}")

    def __str__(self):
        return f"Escuela: {self.name}, Localidad: {self.location}, Responsable: {self.responsible}"

class Person:
    def __init__(self, name, last_name, dni):
        self.name = name
        self.last_name = last_name
        self.dni = dni

    def __str__(self):
        return f"Persona: {self.name} {self.last_name} - DNI: {self.dni}"

class Teacher(Person):
    def __init__(self, name, last_name, dni, subject):
        super().__init__(name, last_name, dni)
        self.subject = subject

    def __str__(self):
        return f"Profesor: {self.name} {self.last_name} - DNI: {self.dni}, Materia: {self.subject}"

class Student(Person):
    def __init__(self, name, last_name, dni, course, responsible_teacher):
        super().__init__(name, last_name, dni)
        self.course = course
        self.responsible_teacher = responsible_teacher

    def __str__(self):
        return f"Alumno: {self.name} {self.last_name} - DNI: {self.dni}, Curso: {self.course}, Profesor Responsable: {self.responsible_teacher}"

# Functions for the menu
def add_school():
    clear()
    name = input("Nombre de la escuela: ")
    location = input("Localidad de la escuela: ")
    responsible = input("Responsable de la escuela: ")
    return School(name, location, responsible)

def show_schools(schools):
    clear()
    if not schools:
        print("No hay escuelas registradas.")
    for school in schools:
        print(school)

def remove_school(schools):
    clear()
    if schools:
        for i, school in enumerate(schools, 1):
            print(f"{i}. {school.name}")
        selection = int(input("Seleccione el número de la escuela a eliminar: ")) - 1
        if 0 <= selection < len(schools):
            school_to_remove = schools.pop(selection)
            print(f"Escuela eliminada: {school_to_remove}")
        else:
            print("Selección no válida.")
    else:
        print("No hay escuelas para eliminar.")

def add_teacher():
    clear()
    name = input("Nombre del profesor: ")
    last_name = input("Apellidos del profesor: ")
    dni = input("DNI del profesor: ")
    subject = input("Materia del profesor: ")
    return Teacher(name, last_name, dni, subject)

def add_student(teachers):
    clear()
    name = input("Nombre del alumno: ")
    last_name = input("Apellidos del alumno: ")
    dni = input("DNI del alumno: ")
    course = input("Curso del alumno: ")

    print("Profesores disponibles:")
    for i, teacher in enumerate(teachers, 1):
        print(f"{i}. {teacher}")

    selection = int(input("Seleccione el número del profesor responsable: ")) - 1
    responsible_teacher = teachers[selection] if 0 <= selection < len(teachers) else None

    return Student(name, last_name, dni, course, responsible_teacher)

# Menu functions
def aggregation_menu(schools, teachers):
    clear()
    print("\nMenú de Agregación:")
    print("a. Agregar Escuela")
    print("b. Agregar Profesor")
    print("c. Agregar Alumno")

    sub_option = input("Seleccione una opción: ")

    if sub_option == "a":
        school = add_school()
        schools.append(school)
    elif sub_option == "b":
        teacher = add_teacher()
        teachers.append(teacher)
    elif sub_option == "c":
        if teachers:
            student = add_student(teachers)
            for school in schools:
                school.add_student(student)
        else:
            print("Debe agregar al menos un profesor antes de agregar un alumno.")
    else:
        print("Opción no válida. Intente de nuevo.")

def show_menu(schools, teachers):
    clear()
    print("\nMenú de Mostrar:")
    print("a. Mostrar Escuelas")
    print("b. Mostrar Profesores")
    print("c. Mostrar Alumnos")

    sub_option = input("Seleccione una opción: ")

    if sub_option == "a":
        show_schools(schools)
    elif sub_option == "b":
        for teacher in teachers:
            print(teacher)
    elif sub_option == "c":
        for school in schools:
            school.show_students()
    else:
        print("Opción no válida. Intente de nuevo.")

def deletion_menu(schools, teachers):
    clear()
    print("\nMenú de Eliminación:")
    print("a. Eliminar Escuela")
    print("b. Eliminar Profesor")
    print("c. Eliminar Alumno")

    sub_option = input("Seleccione una opción: ")

    if sub_option == "a":
        remove_school(schools)
    elif sub_option == "b":
        if teachers:
            for i, teacher in enumerate(teachers, 1):
                print(f"{i}. {teacher}")
            selection = int(input("Seleccione el número del profesor a eliminar: ")) - 1
            if 0 <= selection < len(teachers):
                teacher_to_remove = teachers.pop(selection)
                print(f"Profesor eliminado: {teacher_to_remove}")
                for school in schools:
                    school.remove_teacher(teacher_to_remove)
            else:
                print("Selección no válida.")
        else:
            print("No hay profesores para eliminar.")
    elif sub_option == "c":
        if schools:
            for i, school in enumerate(schools, 1):
                print(f"{i}. {school.name}")
            selection_school = int(input("Seleccione el número de la escuela: ")) - 1
            if 0 <= selection_school < len(schools):
                school = schools[selection_school]
                if school.students:
                    for i, student in enumerate(school.students, 1):
                        print(f"{i}. {student}")
                    selection_student = int(input("Seleccione el número del alumno a eliminar: ")) - 1
                    if 0 <= selection_student < len(school.students):
                        student_to_remove = school.students.pop(selection_student)
                        print(f"Alumno eliminado: {student_to_remove}")
                    else:
                        print("Selección no válida.")
                else:
                    print("No hay alumnos para eliminar.")
            else:
                print("Selección no válida.")
        else:
            print("No hay escuelas para eliminar alumnos.")
    else:
        print("Opción no válida. Intente de nuevo.")

def school_management_menu(schools, teachers):
    clear()
    print("\nMenú de Gestión de Escuelas:")
    print("a. Asignar Profesor a Escuela")
    print("b. Asignar Alumno a Escuela")

    sub_option = input("Seleccione una opción: ")

    if sub_option == "a":
        if schools and teachers:
            for i, school in enumerate(schools, 1):
                print(f"{i}. {school.name}")
            selection_school = int(input("Seleccione el número de la escuela: ")) - 1
            if 0 <= selection_school < len(schools):
                school = schools[selection_school]
                for i, teacher in enumerate(teachers, 1):
                    print(f"{i}. {teacher}")
                selection_teacher = int(input("Seleccione el número del profesor: ")) - 1
                if 0 <= selection_teacher < len(teachers):
                    teacher = teachers[selection_teacher]
                    school.add_teacher(teacher)
                    print(f"Profesor {teacher} asignado a la escuela {school.name}")
                else:
                    print("Selección no válida.")
            else:
                print("Selección no válida.")
        else:
            print("No hay escuelas o profesores para realizar la asignación.")
    elif sub_option == "b":
        if schools and teachers:
            for i, school in enumerate(schools, 1):
                print(f"{i}. {school.name}")
            selection_school = int(input("Seleccione el número de la escuela: ")) - 1
            if 0 <= selection_school < len(schools):
                school = schools[selection_school]
                if teachers:
                    for i, student in enumerate(school.students, 1):
                        print(f"{i}. {student}")
                    selection_student = int(input("Seleccione el número del alumno: ")) - 1
                    if 0 <= selection_student < len(school.students):
                        student = school.students[selection_student]
                        print(f"Alumno {student} asignado a la escuela {school.name}")
                    else:
                        print("Selección no válida.")
                else:
                    print("No hay alumnos para realizar la asignación.")
            else:
                print("Selección no válida.")
        else:
            print("No hay escuelas o profesores para realizar la asignación.")
    else:
        print("Opción no válida. Intente de nuevo.")

# Example usage
schools = []
teachers = []
clear()
while True:
    print("\nMenú:")
    print("1. Agregación")
    print("2. Mostrar")
    print("3. Eliminación")
    print("4. Gestión de Escuelas")
    print("5. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        aggregation_menu(schools, teachers)
    elif option == "2":
        show_menu(schools, teachers)
    elif option == "3":
        deletion_menu(schools, teachers)
    elif option == "4":
        school_management_menu(schools, teachers)
    elif option == "5":
        clear()
        break
    else:
        print("Opción no válida. Intente de nuevo.")
