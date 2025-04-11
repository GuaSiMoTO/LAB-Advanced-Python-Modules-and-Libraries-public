# Iteration 1

from random import uniform
from math import floor, ceil

def abs_number():
    numero = uniform(-100, 0)
    numero_abs = abs(numero)    
    
    # aqui calculo el ceil y floor, que no se lo q es!!
    numero_ceil = ceil(numero_abs)
    numero_floor = floor(numero_abs)
    
    print(f'Decimal aleotorio: {numero}')
    print(f'Numero absoluto: {numero_abs}')
    print(f'Numero rodendeo abajo: {numero_ceil}')
    print(f'Numero rodendeo abajo: {numero_floor}')

abs_number()

# Iteration 2.1 - Display students
def display_students():
    with open('data.txt', 'r') as file:
        for line in file:
            name, email, course, grade = line.strip().split(',')
            print(f"{name} - {email} - {course} - {float(grade):.1f}")

# Iteration 2.2 - Group students by course
def group_students():
    courses = {}
    with open('data.txt', 'r') as file:
        for line in file:
            name, email, course, grade = line.strip().split(',')
            rounded_grade = round(float(grade))
            if course not in courses:
                courses[course] = []
            courses[course].append(f"{name} - {email} - {rounded_grade}")
    
    for course, students in courses.items():
        print(f"\n{course}:")
        for student in students:
            print(student)

# Ejecutar las funciones
print("=== Todos los estudiantes ===")
display_students()

print("\n=== Estudiantes agrupados por curso ===")
group_students()