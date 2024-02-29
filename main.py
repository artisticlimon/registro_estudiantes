import os
from registro_de_estudiantes import RegistroEstudiantes 

# Lista de los id's ya utilizados para que no haya id's repetidos
lista_id = []

def main():
    # Crear la instancia del registro de estudiantes y desplegar el menu
    global registro
    registro = RegistroEstudiantes('estudiantes.txt')
    menu()

def menu():
    global registro
    # Muestra el menu al usuario para que seleccione que quiere hacer
    while True:
        #Lo que visualiza el usuario
        print('\nMenu: ')
        print('1. Agregar estudiante')
        print('2. Visualizar los reportes de todos los estudiantes')
        print('3. Buscar estudiante por ID')
        print('4. Salir')
        seleccion = input('Seleccione una opcion: ')

        # Lo que significa cada opcion
        if seleccion == '1':
            # Agrega un estudiante
           registro.agregar_estudiante(*pedir_datos())
           print('ESTUDIANTE AGREGADO')
        elif seleccion == '2':
            # Visualiza a todos los estudiantes
            registro.visualizar_todos_estudiantes()
        elif seleccion == '3':
            # Busca un estudiante por id
            registro.buscar_estudiante_por_id()
        elif seleccion == '4':
            # Sale del programa
            break
        else:
            # Da un mensaje de error al usuario por dar una opcion invalida
            print(' SELECCION INVALIDA !!! ')

def pedir_datos():
    # Proporciona los atributos al estudiante que se anadira a la lista de estudiantes.

    # Pedir los datos personales
    nombre = input('Ingrese el nombre del estudiante (sin apellido): ')
    apellido= input('Ingrese el apellido del estudiante: ')
    # Pedir id y verificar si ya ha sido utilizado
    id= registro.verificar_id()
    # Pedir correo electronico y verificar si es un correo valido
    correo_electronico= registro.verificar_correo_electronico()

    # Pedir las notas de cada evaluacion usando la funcion pedir_nota()
    evaluaciones = ['tarea 1', 'tarea 2', 'tarea 3', 'tarea 4', 'examen parcial 1', 'examen parcial 2', 'examen parcial 3', 'examen final']
    notas = [pedir_nota(evaluacion) for evaluacion in evaluaciones]

    # Devolver los datos
    return nombre, apellido, id, correo_electronico, notas

def pedir_nota(evaluacion):
    # Pide la nota de cada evaluacion y evalua si cumple con las condiciones de una nota
    while True:
        # Lo que visualiza el usuario para que digite la nota de la evaluacion dada por el parametro 'evaluacion'
        nota = input(f"Por favor ingrese la nota del/a {evaluacion}: ")

        # Evaluar si la nota es un numerica y si esta entre 0 y 100 para revisar si es una nota valida
        if nota.isdigit() and 0<= float(nota)<=100:
            nota = float(nota)
            # Devolver la nota
            return nota
        else:
            print('******* Por favor ingrese una nota valida.')

if __name__ == '__main__':
    main()
