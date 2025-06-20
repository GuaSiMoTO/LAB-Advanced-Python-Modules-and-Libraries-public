# Iteration 1

from random import uniform
from math import floor, ceil

def abs_number():
    numero = uniform(-100, 0)
    numero_abs = abs(numero)    
    
    # floor: redondea hacia abajo y celi: redondea hacia arriba
    numero_ceil = ceil(numero_abs)
    numero_floor = floor(numero_abs)
    
    print(f'Decimal aleotorio: {numero}')
    print(f'Numero absoluto: {numero_abs}')
    print(f'Numero rodendeo abajo: {numero_ceil}')
    print(f'Numero rodendeo abajo: {numero_floor}')

abs_number()

# Iteration 2.1 - Display students
def display_students():
    
    with open('data/data.txt', 'r') as file:
        for line in file:
            name, email, course, grade = line.strip().split(',')
            print(f"{name} - {email} - {course} - {grade}")
            
    print("=== Todos los estudiantes ===")

# Iteration 2.2 - Group students by course
def group_students():
    courses = {}
    with open('data/data.txt', 'r') as file:
        for line in file:
            name, email, course, grade = line.strip().split(',')
    
            if course not in courses:
                courses[course] = []
            courses[course].append(f"{name} - {email} - {grade}")
    
    for course, students in courses.items():
        print(f"\n{course}:")
        for student in students:
            print(student)
            
    print("\n=== Estudiantes agrupados por curso ===")
# Ejecutar las funciones

display_students()

group_students()

# iteration 3: Add students

new_students = ["Tony Stark,iamironman@example.com,Reboot 1,10",
        "Bruce Wayne,iambatman@example.com,Reboot 1,9"]

def add_students(students):
    
    with open("data/data.txt", "a") as f:
        for student in students:
            f.write(student + "\n")
            
    print("=== Añadir estudiantes ===")

# add_students(new_students)

# Iteration 4 / Modify_students

def modify_student(alumno, cambio, num):
    
    with open("data/data.txt", "r") as f:
        lines = f.readlines()
        
    with open("data/data.txt", "w") as f:
        for line in lines:
            if line.startswith(alumno):
                parts = line.strip().split(",")
                parts[num] = cambio  # num: 1,2,3 por si quieres cambiar email, course o grade
                line = ",".join(parts) + "\n"
            f.write(line)
    
    print("=== Alumno Modificado ===")


# modify_student('Olivia Davis', "email@falso.fr", 1)

# BONUS - Improve_your_knowledge

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("data/data.csv")

# Mostrar las primeras 4 filas
print(df.head(4))

# Cambiar el nombre de las dos primeras personas
df.loc[0, "Name"] = "New Name 1"
df.loc[1, "Name"] = "New Name 2"

# Guardar los cambios en el mismo archivo
df.to_csv("data/data.csv", index=False)




