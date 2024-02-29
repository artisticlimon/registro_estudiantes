import os

class Estudiante:
    def __init__(self, nombre, apellido, id, correo_electronico, notas):
        # Datos personales
        self.nombre = nombre  
        self.apellido= apellido 
        self.id= id 
        self.correo_electronico = correo_electronico

        # Notas y porcentajes
        self.notas = notas  
        self.porcentajes = self.calcular_porcentajes(notas)

        # Nota final
        self.nota_final = sum(self.porcentajes)

        # Estado del estudiante
        if self.nota_final >= 75:
            self.estado = 'APROBADO'
        elif 75 > self.nota_final >=60:
            self.estado = 'AMPLIACION'
        else:
            self.estado = 'REPROBADO'

    def calcular_porcentajes(self, notas):
        # Calcula el porcentaje que aporta cada evaluacion
        porcentajes = []
        promedio_parciales = 0
        for i in range(len(notas)):
            if 0<= i <=3:
                porcentajes.append(notas[i]*0.05)
            elif 4<= i <6:
                promedio_parciales += notas[i]
            elif i == 6:
                promedio_parciales += notas[i]
                promedio_parciales*= 1/3
                porcentajes.append(promedio_parciales*0.3)
            else:
                porcentajes.append(notas[i]*0.5) 
        return porcentajes
        
class RegistroEstudiantes:
    def __init__(self, archivo):
        # Archivo en el que se va a guardar la informacion los estudiantes
        self.archivo = archivo
        # Lista en la que se van a guardar los estudiantes
        self.estudiantes = []
        # Lista en la que se guardan los id's para que no haya duplicados
        self.lista_id = []
        # Si el archivo existe, cargarlo
        if os.path.exists(self.archivo):
            self.cargar_estudiantes()

    def cargar_estudiantes(self):
    # Convertir todos las lineas en el archivo a variables y anadirlos a la lista de estudiantes
        
        # Abrir el archivo para leerlo
        with open(self.archivo, 'r') as f:
            # Iterar sobre las lineas del archivo para agregar el objeto estudiante a la lista de estudiantes
            for linea in f:
                nombre, apellido, id, correo_electronico = linea.strip().split(',')[:4]
                notas = [float(x) for x in linea.strip().split(',')[4:]]
                self.lista_id.append(id)
                self.estudiantes.append(Estudiante(nombre, apellido, id, correo_electronico, notas))
    
    def guardar_estudiantes(self):
    # Guardar el estudiante en el archivo como una lista de texto
        
        #Abrir el archivo para modificarlo
        with open(self.archivo, 'w') as f:
            # Iterar sobre la lista de estudiantes para escribir cada contacto en el archivo
            for estudiante in self.estudiantes:
                notas_string = [str(x) for x in estudiante.notas]
                string_temp = ','.join(notas_string)
                f.write(f'{estudiante.nombre},{estudiante.apellido},{estudiante.id},{estudiante.correo_electronico},{string_temp}\n')

    def agregar_estudiante(self, nombre, apellido, id, correo_electronico, notas):
    # Guardar al estudiante nuevo en una lista de contactos y despues escribir su informacion en el archivo de texto
        self.estudiantes.append(Estudiante(nombre, apellido, id, correo_electronico, notas))
        self.guardar_estudiantes()

    def verificar_id(self):
    # Sirve para verificar si el id no ha sido utilizado antes
        id= input('Ingrese el id del estudiante: ')
        # while True:
        #     global self.lista_id
        if id not in self.lista_id:
            # Si no fue utilizado antes, se anade a la lista y ese es el valor que devuelve
            self.lista_id.append(id)
            return id
        else:
            # Si ya fue usado, se pide otro id
            id = input('********Por favor indique un id que no haya sido utilizado antes: ')
        return id

    def verificar_correo_electronico(self):
        # Verifica si el correo electronico es valido (si tiene @)
        correo_electronico= input('Ingrese el correo electronico del estudiante: ')
        while True:
            if '@' and '.' in correo_electronico:
                # Si el correo electronico tiene arroba, es valido y se devuelve como el correo electronico
                return correo_electronico
            else:
                # Si no es valido, se pide otro correo electronico
                correo_electronico = input('*****Por favor indique un correo electronico valido (uno que contenga una @): ')

    def visualizar_todos_estudiantes(self):
    # Despliega los reportes de todos los estudiantes

        # Caso en el que no haya estudiantes en la lista
        if not self.estudiantes:
            print('No hay estudiantes registrados')

        # Desplegar los reportes para cada estudiante en la lista
        else:
            print('*****************')
            print('LISTA DE ESTUDIANTES')
            print('')
            # for i, estudiante in enumerate(self.estudiantes,start=1):
            for estudiante in self.estudiantes:
                print(f'{estudiante.nombre} {estudiante.apellido} id: {estudiante.id}')
                self.imprimir_notas(estudiante)

    def imprimir_notas(self, estudiante):
    # Despliega el reporte de calificaciones de un estudiante  
        indice_porcentaje = 0
        for i in range(8):
            if 0<=i<3:
                print(f'Nota tarea {i+1}: {estudiante.notas[i]}')
            elif i == 3:
                print(f'Nota tarea {i+1}: {estudiante.notas[i]}')
                print(f'PORCENTAJE OBTENIDO DE TAREAS: {estudiante.porcentajes[indice_porcentaje]}')
                indice_porcentaje += 1
            elif 4<= i < 6:
                print(f'Nota examen parcial {i+1}: {estudiante.notas[i]}')
            elif i == 6:
                print(f'Nota examen parcial {i+1}: {estudiante.notas[i]}')
                print(f'PORCENTAJE OBTENIDO DE LOS EXAMENES PACIALES: {estudiante.porcentajes[indice_porcentaje]}')
                indice_porcentaje += 1    
            else:
                print(f'Nota examen final: {estudiante.notas[i]}')
                print(f'PORCENTAJE OBTENIDO DEL EXAMEN FINAL: {estudiante.porcentajes[indice_porcentaje]}')  
        print('***************************')
        print(f'NOTA FINAL = {round(estudiante.nota_final, 2)}')
        print(f'ESTADO: {estudiante.estado}')
        print('***************************')

    def buscar_estudiante_por_id(self):
    # Busca al estudiante que tiene el id proporcionado por el usuario 

        # Pide el id al usuario
        id_a_buscar = input('Por favor ingrese el id a buscar: ')

        # Busca una coincidencia en la lista de estudiantes
        hay_estudiante = False
        for estudiante in self.estudiantes:
            # Define que pasa si hay una coincidencia
            if estudiante.id == id_a_buscar:
                print(' ***** ESTUDIANTE ENCONTRADO ***** ')
                print(f'ID: {estudiante.id}')
                print(f'{estudiante.nombre} {estudiante.apellido}')
                print(f'ESTADO= {estudiante.estado}')
                # Si hay estudiante entonces se cambia la variable de si hay estudiante a True
                hay_estudiante = True
                # Preguntar al usuario si desea que se le muestre el reporte de ese estudiante
                self.desea_mostrar_reporte(estudiante)
        # Si el estudiante con ese id no existe, se imprime ese mensaje
        if not hay_estudiante:
            print('************No existe un estudiante con ese ID')

    def desea_mostrar_reporte(self, estudiante):
    # Pregunta al usuario si desea visualizar el reporte del estudiante dado por el parametro
        while True:
            # Preguntar al usuario si quiere o no visualizar el reporte
            desea_mostrar_reporte= input('Desea visualizar el reporte del estudiante? \n 1. Si \n 2. No \n')

            # Lo que significa cada opcion
            if desea_mostrar_reporte == '1':
                # Pide desplegar el reporte del estudiante
                self.visualizar_un_reporte(estudiante)
                break
            if desea_mostrar_reporte == '2':
                # Termina de ejecutarse la funcion sin hacer nada
                break
            else:
                # Despliega un mensaje de error porque la opcion digitada no es valida
                print('Ingrese una opcion valida')

    def visualizar_un_reporte(self, estudiante_encontrado):
        # Despliega el reporte de un estudiante en especifico

        # Recorre la lista de estudiantes para encontrar el estudiante buscado
        for estudiante in self.estudiantes:
            if estudiante == estudiante_encontrado:
                # Una vez que se encuentra el estudiante, despliega su reporte
                self.imprimir_notas(estudiante)     
